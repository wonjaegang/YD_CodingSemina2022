import pygame
from math import *
from pygame.locals import *
import sys
sys.setrecursionlimit(10**7)

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
        return self.obstacles


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

    # def set_motor_value(self, obstacles):
    #     self.right_wheel, self.left_wheel = self.DWA(obstacles)

    def obstacles(self):
        obstacles = []
        for degree, distance in enumerate(self.LiDAR_data):
            if distance:
                obstacles.append([self.x + cos(self.heading + radians(degree)) * distance,
                                  self.y + sin(self.heading + radians(degree)) * distance])
        return obstacles

    def DWA(self, obstacles):
        cur_v = [self.right_wheel, self.left_wheel]
        dynamic_window = [[[0 for _ in range(2)] for _ in range(7)] for _ in range(7)]
        for i in range(7):
            for j in range(7):
                dynamic_window[i][j] = [cur_v[0] + self.max_a / 3 * (i - 3), cur_v[1] + self.max_a / 3 * (j - 3)]

        def objective_function(heading, right_wheel, left_wheel):
            virtual_pos_x, virtual_pos_y, virtual_heading = self.x, self.y, self.heading
            count, max_count = 0, 100

            while True:
                r = self.wheel_radius
                L = self.tread / 2
                d_x = cos(heading) * r * 0.5 * (right_wheel + left_wheel)
                d_y = sin(heading) * r * 0.5 * (right_wheel + left_wheel)
                d_theta = r * 0.5 * (right_wheel - left_wheel) / L
                virtual_pos_x += d_x
                virtual_pos_y += d_y
                virtual_heading += d_theta

                def virtual_LiDAR(obstacle):
                    data_list = [0.0 for _ in range(360)]
                    for direction in range(0, 360):
                        angle = (virtual_heading + radians(direction)) % (pi * 2)
                        x_positive = False if pi / 2 <= angle < pi / 2 * 3 else True
                        y_positive = True if 0 <= angle < pi else False
                        distance = []
                        x_index = virtual_pos_x // GRID_SIZE_X + x_positive
                        while True:
                            if x_index == GRID_NUM_X * x_positive:
                                break
                            else:
                                x_value = x_index * GRID_SIZE_X
                                y_value = tan(angle) * (x_value - virtual_pos_x) + virtual_pos_y
                                y_index = y_value // GRID_SIZE_Y
                                if not 0 < y_index < GRID_NUM_Y:
                                    break
                                if [x_index + x_positive - 1, y_index] in obstacle:
                                    distance.append(
                                        sqrt((x_value - virtual_pos_x) ** 2 + (y_value - virtual_pos_y) ** 2))
                                    break
                                x_index += x_positive * 2 - 1

                        y_index = virtual_pos_y // GRID_SIZE_Y + y_positive
                        while True:
                            if y_index == GRID_NUM_Y * y_positive:
                                break
                            else:
                                y_value = y_index * GRID_SIZE_Y
                                x_value = (y_value - virtual_pos_y) / tan(angle) + virtual_pos_x if tan(
                                    angle) else X_MAX
                                x_index = x_value // GRID_SIZE_X
                                if not 0 < x_index < GRID_NUM_X:
                                    break
                                if [x_index, y_index + y_positive - 1] in obstacle:
                                    distance.append(
                                        sqrt((x_value - virtual_pos_x) ** 2 + (y_value - virtual_pos_y) ** 2))
                                    break
                                y_index += y_positive * 2 - 1
                        data_list[direction] = min(distance) if distance else 0
                    return data_list
                count += 1
                if not min(virtual_LiDAR(obstacles)) or \
                        170 <= abs(heading - virtual_heading) <= 190 * pi or count >= max_count:
                    break

            objective_function(self.heading, *dynamic_window[i][j])
            w1 = 1 - count / max_count
            w2 = abs(atan2(self.goal_x - virtual_pos_x, self.goal_y - virtual_pos_y) - virtual_heading) / pi
            return 0.5 * w1 + 0.5 * w2

        cost_list = []
        for i in range(7):
            for j in range(7):
                cost_list.append([objective_function(self.heading, *dynamic_window[i][j]), i, j])
        self.right_wheel, self.left_wheel = dynamic_window[min(cost_list, key=lambda x: x[0])[1]][min(cost_list, key=lambda x: x[0])[2]]
        # return dynamic_window[min(cost_list, key=lambda x: x[0])[1]][min(cost_list, key=lambda x: x[0])[2]]

            # 왼쪽, 오른쪽 속도로 Dynamic window 설정
            # 각각의 속도(v_l, v_r)를 모두 넣은 리스트를 만들어 함수에 넣기
            # 루프를 돌려 미래 상황 예측 -> 다음 상황이 문제가 없다면 count += 1
            # (1)count가 가장 높을수록, (2)그 미래 상황이 목표와 각도 차이가 작을수록 낮은 비용 부여
            # 낮은 비용의 속도(v_l, v_r) 선택


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
        car.DWA(grid_map.obstacles)
        car.move()

        pygame.display.flip()
        clock.tick(rate)
        count += 1


if __name__ == '__main__':
    main()
