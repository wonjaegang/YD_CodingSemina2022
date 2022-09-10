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

    def GUI_display(self):
        a = atan2(self.width, self.length)
        b = sqrt(self.length ** 2 + self.width ** 2) / 2
        corner1 = [self.x + cos(self.heading - a) * b, Y_MAX - (self.y + sin(self.heading - a) * b)]
        corner2 = [self.x + cos(self.heading + a) * b, Y_MAX - (self.y + sin(self.heading + a) * b)]
        corner3 = [self.x + cos(self.heading + pi - a) * b, Y_MAX - (self.y + sin(self.heading + pi - a) * b)]
        corner4 = [self.x + cos(self.heading + pi + a) * b, Y_MAX - (self.y + sin(self.heading + pi + a) * b)]
        pygame.draw.polygon(screen, RED, [corner1, corner2, corner3, corner4])

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
        # 즉 0은 받지 않겠다 / 측정되지 않은 것들은 obstacles에 받지 않겠다 이유: 장애물들의 절대좌표를 받는 것이라 필요가 없다
        obstacles = []
        for degree, distance in enumerate(self.LiDAR_data):
            if distance:
                obstacles.append([self.x + cos(self.heading + radians(degree)) * distance,
                                  self.y + sin(self.heading + radians(degree)) * distance])
        return obstacles

    def DWA(self):
        weight1 = 1
        weight2 = 1
        # 장애물 비용함수 맞춰주기 용 상수
        obstacle_force = 100

        # 비용함수 정하기
        def cost_function(pos):
            cost1 = sqrt((pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2)
            obstacle_min_distance = min([sqrt((pos[0] - obstacle[0]) ** 2 + (pos[1] - obstacle[1]) ** 2) for
                                         obstacle in self.obstacles()])
            cost2 = obstacle_force - obstacle_min_distance
            return cost1 * weight1 + cost2 * weight2

        # 미래 속도 값 정하기
        DWA_size = 5
        DWA_step = 2 * self.max_a / (DWA_size - 1)
        DWA_right_v = [self.right_wheel - self.max_a + DWA_step * i for i in range(DWA_size) if
                       abs(self.right_wheel - self.max_a + DWA_step * i) <= self.max_v]
        DWA_left_v = [self.left_wheel - self.max_a + DWA_step * i for i in range(DWA_size) if
                      abs(self.left_wheel - self.max_a + DWA_step * i) <= self.max_v]

        # 타임스톤 몇 번 허쉴?
        set_timestone = 10

        # 미래의 위치 값을 받아야함 만들어진 속도들을 바탕으로 각각을 get.velocity 함수에 넣어 파악할 수 있다. -> x, y 좌표와 헤딩을,,
        # 각 바퀴들의 속도 조합마다의 미래 x, y, heading 필요
        best_cost = float('inf')
        best_vel = [self.right_wheel, self.left_wheel]
        for right_v in DWA_right_v:
            for left_v in DWA_left_v:
                pos_future = [self.x, self.y, self.heading]
                for _ in range(set_timestone):
                    rate_of_change = self.get_velocity(pos_future[-1], right_v, left_v)
                    pos_future = [pos + rate_of_change for pos, rate_of_change in zip(pos_future, rate_of_change)]
                cost = cost_function(pos_future[:2])
                if cost < best_cost:
                    best_cost = cost
                    best_vel = [right_v, left_v]
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
