"""
주어진 함수 print_grid_map() 을 완성해보자.

print_grid_map()은 가상의 라이다 virtual_lidar() 로부터 1도의 간격으로 거리값이 담긴 길이 360개의 거리값을 배열로 받는다.
그 후, 10X10 그리드맵을 출력한다. 장애물(마우스)가 존재하는 좌표는 X로, 아닌 좌표는 O로 나타내어보자.

그리드맵의 실제크기는 500X500이며, 그리드맵의 중심에 라이다가 존재한다.
중심기준 오른쪽 수평직선에서 0도로 시작하고, 반시계 방향으로 359까지 증가한다.

단, print_grid_map() 에 인자로 주어진 sensor_data 의 값만 사용하자. 가공할 수 있는 값들은 sensor_data 의 360개의 값이 전부다.

"""

import pygame
from math import*
from pygame.locals import *

pygame.init()
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
rate = 50


class Obstacle:
    def __init__(self, CenterX, centerY, width, height):
        self.rect = pygame.rect.Rect(0, 0, width, height)
        self.rect.centerx = CenterX
        self.rect.centery = 500 - centerY

    def GUI_display(self):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)


# 주어진 속력과 방향에 따라 등속운동하는 자동차
# 좌표계의 좌측 하단이 0, 0 이다. 우측 방향이 x+, 위쪽 방향이 y+.
class Car:
    def __init__(self, initial_location):
        self.x, self.y = initial_location
        self.direction = 0
        self.velocity = 1

        self.size = 10
        self.rect = pygame.rect.Rect(0, 0, self.size, self.size)

    def autonomous_drive(self):
        pass

    def move(self):
        self.x += self.velocity * cos(self.direction)
        self.y += self.velocity * sin(self.direction)

    def GUI_display(self):
        self.rect.centerx = self.x
        self.rect.centery = 500 - self.y
        pygame.draw.rect(screen, (0, 0, 0), self.rect)

    def set_velocity(self):
        self.velocity = 1

    def set_steer(self):
        self.direction = 3.141592 / 2


def main():
    car = Car([250, 0])  # x, y
    obstacle = Obstacle(250, 250, 50, 5)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return 0

        car.set_velocity()
        car.set_steer()
        car.move()

        if pygame.rect.Rect.colliderect(car.rect, obstacle.rect):
            pygame.quit()
            return 0

        screen.fill((255, 255, 255))
        car.GUI_display()
        obstacle.GUI_display()

        pygame.display.flip()
        clock.tick(rate)


if __name__ == '__main__':
    main()
