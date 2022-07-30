"""
자동차는 이제 라이다를 갖게 되었다. 장애물을 회피해보자.
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
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
rate = 100


class GridMap:
    def __init__(self):
        with open("grid_map", "r") as f:
            self.map = f.readlines()
        self.map = list(map(lambda x: x.split('\n')[0].split(' '), self.map))
        self.starting_point = []
        self.goal_point = []
        self.GUI_display()

    def GUI_display(self):
        for row, line in enumerate(self.map):
            for column, ch in enumerate(line):
                if ch == 'X':
                    pygame.draw.rect(screen, BLACK, [50 * column, 50 * row, 50, 50])
                elif ch == '1':
                    pygame.draw.circle(screen, GREEN, [50 * column + 25, 50 * row + 25], 10)
                    self.starting_point = [50 * column + 25, 500 - (50 * row + 25)]
                elif ch == '2':
                    pygame.draw.circle(screen, BLUE, [50 * column + 25, 50 * row + 25], 10)
                    self.goal_point = [50 * column + 25, 500 - (50 * row + 25)]
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
        corner1 = [self.x + cos(self.heading - a) * b, 500 - (self.y + sin(self.heading - a) * b)]
        corner2 = [self.x + cos(self.heading + a) * b, 500 - (self.y + sin(self.heading + a) * b)]
        corner3 = [self.x + cos(self.heading + pi - a) * b, 500 - (self.y + sin(self.heading + pi - a) * b)]
        corner4 = [self.x + cos(self.heading + pi + a) * b, 500 - (self.y + sin(self.heading + pi + a) * b)]
        pygame.draw.polygon(screen, RED, [corner1, corner2, corner3, corner4])

    def set_motor_value(self, count):
        self.right_wheel = 2.3
        self.left_wheel = 2

    def LiDAR(self):
        data_list = [0.0 for _ in range(360)]
        for direction in range(360):
            angle = (self.heading + radians(direction)) % (pi * 2)
            if atan2(HEIGHT - self.y, WIDTH - self.x) < angle <= atan2(HEIGHT - self.y, 0 - self.x):
                final_point = [self.x + (HEIGHT - self.y) / tan(angle), HEIGHT]
            elif atan2(HEIGHT - self.y, 0 - self.x) < angle <= atan2(0 - self.y, 0 - self.x) % (pi * 2):
                final_point = [0, self.y + (0 - self.x) * tan(angle)]
            elif atan2(0 - self.y, 0 - self.x) % (pi * 2) < angle <= atan2(0 - self.y, WIDTH - self.x) % (pi * 2):
                final_point = [self.x + (0 - self.y) / tan(angle), 0]
            else:
                final_point = [WIDTH, self.y + (WIDTH - self.x) * tan(angle)]
            pygame.draw.circle(screen, RED, list(map(lambda x: int(x), final_point)), 5)

        return data_list


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

        car.LiDAR()

        pygame.display.flip()
        clock.tick(rate)
        count += 1


if __name__ == '__main__':
    main()
