"""
자동차는 이제 실제 차량과 점점 더 흡사해진다.
차량은 각각 왼쪽/오른쪽 바퀴를 가지고 있으며, 각 바퀴의 속력을 설정해주어 구동시킨다.

"""

import pygame
from math import*
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
rate = 50


class Obstacle:
    def __init__(self, initial_location, size):
        self.rect = pygame.rect.Rect(0, 0, *size)
        self.x, self.y = initial_location

    def GUI_display(self):
        self.rect.centerx = self.x
        self.rect.centery = 500 - self.y
        pygame.draw.rect(screen, BLACK, self.rect)


# 좌표계의 좌측 하단이 0, 0 이다. 우측 방향이 x+, 위쪽 방향이 y+
class Car:
    def __init__(self, initial_location):
        self.x, self.y = initial_location
        self.heading = 0
        self.right_wheel = 0
        self.left_wheel = 0

        self.length = 15
        self.width = 10
        self.tread = 10
        self.wheel_radius = 1

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
        self.right_wheel = 5
        self.left_wheel = 0

    def Lidar(self):
        pass


def main():
    car = Car([250, 125])  # x, y
    obstacle = Obstacle([250, 250], [50, 10])  # (x, y), (width, height)
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return 0

        car.set_motor_value(count)
        car.move()

        screen.fill(WHITE)
        car.GUI_display()
        obstacle.GUI_display()

        pygame.display.flip()
        clock.tick(rate)
        count += 1


if __name__ == '__main__':
    main()
