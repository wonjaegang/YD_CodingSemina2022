"""
굉장히 단순화된 자동차 모델이 있다.
기준좌표계 기준 방향과 속도를 입력해주어 구동시킨다.
좌표계의 좌측 하단이 0, 0 이다. 우측 방향이 x+, 위쪽 방향이 y+이다.

자동차를 1) 정사각형 경로로 2) 랜덤 경로로 움직여보자.

"""

import pygame
from math import*
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
rate = 50


# 주어진 속력과 방향에 따라 등속운동하는 자동차
# 좌표계의 좌측 하단이 0, 0 이다. 우측 방향이 x+, 위쪽 방향이 y+.
# direction 은 기준좌표계를 따른다.
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
        self.velocity = 1

    def set_steer(self, count):
        self.direction = count / 100


def main():
    car = Car([250, 125])  # x, y
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

        pygame.display.flip()
        clock.tick(rate)
        count += 1


if __name__ == '__main__':
    main()
