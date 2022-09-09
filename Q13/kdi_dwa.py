"""
자동차는 이제 라이다를 갖게 되었다. 장애물을 회피해보자.
라이다는 차량이 바라보는 방향에서 0도로 시작한다.
장애물을 생성하는 txt 파일 또한 추가하였다.

Q. 협로주행을 통해 목적에 도달하자.

"""

import pygame
from math import *
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
X_MAX = 1000
Y_MAX = 1000
GRID_NUM_X = 10
GRID_NUM_Y = 10
GRID_SIZE_X = int(X_MAX / GRID_NUM_X)
GRID_SIZE_Y = int(X_MAX / GRID_NUM_Y)
screen = pygame.display.set_mode((X_MAX, Y_MAX))
clock = pygame.time.Clock()
rate = 100


class GridMap:
    def __init__(self):
        with open("grid_map", "r") as f:
            self.map = f.readlines()
        self.map = list(map(lambda x: x.split('\n')[0].split(' '), self.map))
        self.starting_point = []
        self.goal_point = []
        self.obstacles = []

        self.GUI_display()

    def GUI_display(self):
        self.obstacles = []
        for row, line in enumerate(self.map):
            for column, ch in enumerate(line):
                if ch == 'X':
                    self.obstacles.append([column, GRID_NUM_Y - row - 1])
                    pygame.draw.rect(screen, BLACK, (GRID_SIZE_X * column, GRID_SIZE_Y * row, GRID_SIZE_X, GRID_SIZE_Y))
                elif ch == '1':
                    pygame.draw.circle(screen, GREEN,
                                       [int(GRID_SIZE_X * (column + 0.5)), int(GRID_SIZE_Y * (row + 0.5))], 10)
                    self.starting_point = [int(GRID_SIZE_X * (column + 0.5)), int(Y_MAX - (GRID_SIZE_Y * (row + 0.5)))]
                elif ch == '2':
                    pygame.draw.circle(screen, BLUE,
                                       [int(GRID_SIZE_X * (column + 0.5)), int(GRID_SIZE_Y * (row + 0.5))], 10)
                    self.goal_point = [int(GRID_SIZE_X * (column + 0.5)), int(Y_MAX - (GRID_SIZE_Y * (row + 0.5)))]
                else:
                    pass


# 좌표계의 좌측 하단이 0, 0 이다. 우측 방향이 x+, 위쪽 방향이 y+
class Car:
    def __init__(self, initial_location, goal_location):
        self.x, self.y = initial_location
        self.goal_x, self.goal_y = goal_location

        self.length = 15
        self.width = 10
        self.tread = 10
        self.wheel_radius = 1
        self.max_a = 1
        self.max_v = 5

        self.heading = 0
        self.right_wheel = 0
        self.left_wheel = 0
        self.last_velocity = 0
        self.trigger = 0

        self.LiDAR_data = []

    def get_velocity(self, heading, right_wheel, left_wheel):
        r = self.wheel_radius
        L = self.tread / 2
        d_x = cos(heading) * r * 0.5 * (right_wheel + left_wheel)
        d_y = sin(heading) * r * 0.5 * (right_wheel + left_wheel)
        d_theta = r * 0.5 * (right_wheel - left_wheel) / L
        return d_x, d_y, d_theta

    def move(self):
        d_x, d_y, d_theta = self.get_velocity(self.heading, self.right_wheel, self.left_wheel)
        self.x += d_x
        self.y += d_y
        self.heading += d_theta
        return self.x, self.y, self.heading

    def GUI_display(self):
        a = atan2(self.width, self.length)
        b = sqrt(self.length ** 2 + self.width ** 2) / 2
        corner1 = [self.x + cos(self.heading - a) * b, Y_MAX - (self.y + sin(self.heading - a) * b)]
        corner2 = [self.x + cos(self.heading + a) * b, Y_MAX - (self.y + sin(self.heading + a) * b)]
        corner3 = [self.x + cos(self.heading + pi - a) * b, Y_MAX - (self.y + sin(self.heading + pi - a) * b)]
        corner4 = [self.x + cos(self.heading + pi + a) * b, Y_MAX - (self.y + sin(self.heading + pi + a) * b)]
        pygame.draw.polygon(screen, RED, [corner1, corner2, corner3, corner4]
                            )

    def LiDAR(self, obstacles, resolution=1):
        data_list = [0.0 for _ in range(360)]
        for direction in range(0, 360, resolution):
            angle = (self.heading + radians(direction)) % (pi * 2)
            x_positive = False if pi / 2 <= angle < pi / 2 * 3 else True
            y_positive = True if 0 <= angle < pi else False
            distance = []
            x_index = self.x // GRID_SIZE_X + x_positive
            while True:
                if x_index == GRID_NUM_X * x_positive:
                    break
                else:
                    x_value = x_index * GRID_SIZE_X
                    y_value = tan(angle) * (x_value - self.x) + self.y
                    y_index = y_value // GRID_SIZE_Y
                    if not 0 < y_index < GRID_NUM_Y:
                        break
                    if [x_index + x_positive - 1, y_index] in obstacles:
                        distance.append(sqrt((x_value - self.x) ** 2 + (y_value - self.y) ** 2))
                        break
                    x_index += x_positive * 2 - 1

            y_index = self.y // GRID_SIZE_Y + y_positive
            while True:
                if y_index == GRID_NUM_Y * y_positive:
                    break
                else:
                    y_value = y_index * GRID_SIZE_Y
                    x_value = (y_value - self.y) / tan(angle) + self.x if tan(angle) else X_MAX
                    x_index = x_value // GRID_SIZE_X
                    if not 0 < x_index < GRID_NUM_X:
                        break
                    if [x_index, y_index + y_positive - 1] in obstacles:
                        distance.append(sqrt((x_value - self.x) ** 2 + (y_value - self.y) ** 2))
                        break
                    y_index += y_positive * 2 - 1
            data_list[direction] = min(distance) if distance else 0

        # for direction, data in enumerate(data_list):
        #     if data:
        #         pygame.draw.line(screen,
        #                          RED,
        #                          [self.x, Y_MAX - self.y],
        #                          [self.x + data * cos(self.heading + radians(direction)),
        #                           Y_MAX - (self.y + data * sin(self.heading + radians(direction)))])
        self.LiDAR_data = data_list

    def set_motor_value(self, count):
        self.right_wheel, self.left_wheel = self.DWA()

    def obstacles(self):
        obstacles = []
        for degree, distance in enumerate(self.LiDAR_data):
            if distance:
                obstacles.append([self.x + cos(self.heading + radians(degree)) * distance,
                                  self.y + sin(self.heading + radians(degree)) * distance])
        return obstacles

    def DWA(self):

        global left_wheel_avg, right_wheel_avg
        c_obstacle_left = 0
        c_obstacle_right = 0

        # 도착 시 정지
        if abs(self.goal_x - self.x) < 10 and abs(self.goal_y - self.y) < 10:
            self.left_wheel = 0
            self.right_wheel = 0
        # 초기 속도 지정 / 그 이후는  속도로 초기 속도 초기화
        else:
            if self.trigger == 0:
                velocity_left_init = 0.00000001
                velocity_right_init = 0.00000001

                self.trigger += 1
                print("wwwwww")
            else:
                velocity_right_init, velocity_left_init = self.last_velocity

            print(velocity_right_init, velocity_left_init)

            a_max = 0.000000001

            s_num = 5
            s_step = 2*a_max/(s_num-1)

            velocity = []
            print('1')
            for i in range(s_num):
                for j in range(s_num):
                    velocity_right = velocity_right_init + s_step*i
                    velocity_left = velocity_left_init + s_step*j
                    velocity.append([velocity_right, velocity_left])

            print(velocity)

            # velocity 다 들어갔음
            distance_list = []

            for k in range(s_num**2):
                d_x, d_y, d_theta = self.get_velocity(self.heading, velocity[k][0], velocity[k][1])
                self.x += d_x
                self.y += d_y
                self.heading += d_theta

                # 가능한 속도로 움직였을 때의 위치를 통한 목표까지 거리
                distance_list.append(sqrt((self.goal_x - self.x)**2 + (self.goal_y - self.y)**2))

            # distance_list 최소값에 해당하는 인덱스 찾기
            index_future = distance_list.index(min(distance_list))
            print(index_future)
            # 이에 해당하는 속도 찾기
            velocity_future_right, velocity_future_left = velocity[index_future]
            #####################################################################################
            # 왼쪽 바퀴에 넣을 가중치
            for i in range(60):
                c_obstacle_left += 1 / (self.LiDAR_data[i] ** 2 + 1)

            # 차 기준 정면 좌측 (반시계 방향 기준 / 0 ~ 60도 [ 1 / (거리의 제곱)]의 평균
            left_wheel_avg = c_obstacle_left / 60

            # 우측 바퀴에 넣을 가중치
            for j in range(300, 360):
                c_obstacle_right += 1 / (self.LiDAR_data[j] ** 2 + 1)

            # 차 기준 정면 우측 (시계 방향 기준 / 0 ~ 60도 [ 1 / (거리의 제곱)]의 평균
            right_wheel_avg = c_obstacle_right / 60
            ######################################################################################

            # 장애물 가중치, 거리 가중치
            obstacle_weight = 0.05
            distance_weight = 1

            self.right_wheel = c_obstacle_right * obstacle_weight + velocity_future_right * distance_weight
            self.left_wheel = c_obstacle_left * obstacle_weight + velocity_future_left * distance_weight

            best_vel = [self.right_wheel, self.left_wheel]
            print(best_vel)
            self.last_velocity = best_vel

            return best_vel

def main():
    grid_map = GridMap()
    car = Car(grid_map.starting_point, grid_map.goal_point)
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return 0

        screen.fill(WHITE)
        grid_map.GUI_display()
        car.GUI_display()

        car.LiDAR(grid_map.obstacles)
        car.set_motor_value(count)
        car.move()

        pygame.display.flip()
        clock.tick(rate)
        count += 1


if __name__ == '__main__':
    main()
