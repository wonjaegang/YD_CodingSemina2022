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

        self.heading = 0
        self.right_wheel = 0
        self.left_wheel = 0
        self.speed = 2
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
        if abs(self.goal_x - self.x) <= 10 and abs(self.goal_y - self.y) <= 10:
            self.right_wheel = 0
            self.left_wheel = 0
            return

        front_data = self.LiDAR_data[266:] + self.LiDAR_data[:95]  # (266 ~ 359 데이터) + (0 ~ 94 데이터) = 189 개의 데이터
        avg_front_data = [0.0 for _ in range(181)]
        for i in range(181):
            avg_front_data[i] = round(sum(front_data[i:(i + 9)]) / 9, 2)  # 주변 9개 데이터 의 평균을 낸 181 개의 평균 데이터
        theta = avg_front_data.index(max(avg_front_data))

        r_cost1, l_cost1, r_cost2, l_cost2, total_r_cost, total_l_cost = 0, 0, 0, 0, 0, 0
        if theta <= 90:
            l_cost1 = theta / 90
        else:
            r_cost1 = (theta - 90) / 90

        if 0 < avg_front_data[0] - avg_front_data[180]:
            l_cost2 = abs(avg_front_data[0] - avg_front_data[180]) / 250
            if 1 < l_cost2:
                l_cost2 = 1
        else:
            r_cost2 = abs(avg_front_data[0] - avg_front_data[180]) / 250
            if 1 < r_cost2:
                r_cost2 = 1

        for i in range(9):
            if 90 - 10 * (i + 1) < theta <= 90 - 10 * i or 90 + 10 * i < theta <= 90 + 10 * (i + 1):
                total_r_cost = 1 / 8 * i * r_cost1 + (1 - 1 / 8 * i) * r_cost2
                total_l_cost = 1 / 8 * i * l_cost1 + (1 - 1 / 8 * i) * l_cost2
                break

        velocity_r = total_r_cost * (2 * self.speed - self.speed) + self.speed
        velocity_l = total_l_cost * (2 * self.speed - self.speed) + self.speed
        self.right_wheel = velocity_r
        self.left_wheel = velocity_l


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