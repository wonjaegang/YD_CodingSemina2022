"""
자동차는 이제 라이다를 갖게 되었다. 장애물을 회피해보자.
라이다는 차량이 바라보는 방향에서 0도로 시작한다.
장애물을 생성하는 txt 파일 또한 추가하였다.

"""

import pygame
from math import*
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
X_MAX = 500
Y_MAX = 500
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
        self.rect = []

        self.GUI_display()

    def GUI_display(self):
        self.rect = []
        for row, line in enumerate(self.map):
            for column, ch in enumerate(line):
                if ch == 'X':
                    self.rect.append(pygame.Rect(GRID_SIZE_X * column, GRID_SIZE_Y * row, GRID_SIZE_X, GRID_SIZE_Y))
                    pygame.draw.rect(screen, BLACK, self.rect[-1])
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

    def get_velocity(self):
        r = self.wheel_radius
        L = self.tread / 2
        d_x = cos(self.heading) * r * 0.5 * (self.right_wheel + self.left_wheel)
        d_y = sin(self.heading) * r * 0.5 * (self.right_wheel + self.left_wheel)
        d_theta = r * 0.5 * (self.right_wheel - self.left_wheel) / L
        return d_x, d_y, d_theta

    def move(self):
        d_x, d_y, d_theta = self.get_velocity()
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

    def LiDAR(self, obstacle_rect_list, resolution=6):
        data_list = [0.0 for _ in range(360)]
        # for direction in range(0, 360, resolution):
        #     angle = (self.heading + radians(direction)) % (pi * 2)
        #     for obstacle_rect in obstacle_rect_list:
        #         xk = obstacle_rect.centerx
        #         yk = obstacle_rect.centerx
        #         k = (cos(angle) ** 2) * (xk - self.x + tan(angle) * (yk - self.y))
        #         xp = self.x + k
        #         yp = self.y + k * tan(angle)
        #         if obstacle_rect.collidepoint(xp, yp):
        #             if angle == 0:
        #                 angle = 0.0000000000000000000000000001
        #             cross = []
        #             left = xk // GRID_SIZE_X * GRID_SIZE_X
        #             bottom = yk // GRID_SIZE_Y * GRID_SIZE_Y
        #             if bottom <= tan(angle) * (left - self.x) + self.y <= bottom + GRID_SIZE_Y:
        #                 cross.append([left, tan(angle) * (left - self.x) + self.y])
        #             if bottom <= tan(angle) * (left + GRID_SIZE_X - self.x) + self.y <= bottom + GRID_SIZE_Y:
        #                 cross.append([left + GRID_SIZE_X, tan(angle) * (left + GRID_SIZE_X - self.x) + self.y])
        #             if left <= (bottom - self.y) / tan(angle) + self.x <= left + GRID_SIZE_X:
        #                 cross.append([bottom, (bottom - self.y) / tan(angle) + self.x])
        #             if left <= (bottom + GRID_SIZE_Y - self.y) / tan(angle) + self.x <= left + GRID_SIZE_X:
        #                 cross.append([bottom + GRID_SIZE_Y, (bottom + GRID_SIZE_Y - self.y) / tan(angle) + self.x])
        #             distance = float('inf')
        #             for point in cross:
        #                 temp = sqrt((self.x - point[0]) ** 2 + (self.y - point[1]) ** 2)
        #                 if temp < distance:
        #                     distance = temp
        #             data_list[direction] = distance
        #
        # for direction, data in enumerate(data_list):
        #     if data:
        #         if data != float('inf'):
        #             pygame.draw.line(screen,
        #                              RED,
        #                              [self.x, 500 - self.y],
        #                              [self.x + data * cos(radians(direction)), 500 - (self.y + data * sin(radians(direction)))])
        return data_list

    def set_motor_value(self, count):
        self.right_wheel = 0
        self.left_wheel = 0


def main():
    grid_map = GridMap()
    car = Car(grid_map.starting_point, grid_map.goal_point)
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return 0

        car.set_motor_value(count)
        car.move()

        screen.fill(WHITE)
        grid_map.GUI_display()
        car.GUI_display()

        # car.LiDAR(grid_map.rect)

        pygame.display.flip()
        clock.tick(rate)
        count += 1


if __name__ == '__main__':
    main()
