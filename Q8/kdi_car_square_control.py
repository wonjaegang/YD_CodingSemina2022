import pygame
from math import*
from pygame.locals import *
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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


# 주어진 속력과 방향에 따라 등속운동하는 자동차
# 좌표계의 좌측 하단이 0, 0 이다. 우측 방향이 x+, 위쪽 방향이 y+.
class Car:
    def __init__(self, initial_location):
        self.x, self.y = initial_location
        self.direction = 0
        self.velocity = 1

        self.size = 10
        self.rect = pygame.rect.Rect(0, 0, self.size, self.size)

    def move(self):
        self.x += self.velocity * cos(self.direction)
        self.y += self.velocity * sin(self.direction)

    def GUI_display(self):
        self.rect.centerx = self.x
        self.rect.centery = 500 - self.y
        pygame.draw.rect(screen, BLACK, self.rect)

    def set_velocity(self, count):
        self.velocity = 5

    def set_steer(self, count):
        if count > 1:
            print(round(self.x + self.y))
            if round(self.x + self.y) == 200 or round(self.x + self.y) == 500 or round(self.x + self.y) == 800:
                self.direction += math.pi / 2


    def Lidar(self):
        pass


def main():
    car = Car([100, 100])  # x, y
    obstacle = Obstacle([250, 250], [50, 10])  # (x, y), (width, height)
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return 0

        car.set_velocity(count)
        car.set_steer(count)
        car.move()

        screen.fill(WHITE)
        car.GUI_display()
        obstacle.GUI_display()

        pygame.display.flip()
        clock.tick(rate)
        count += 1


if __name__ == '__main__':
    main()
