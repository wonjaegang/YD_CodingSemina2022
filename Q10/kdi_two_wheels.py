"""
자동차는 이제 실제 차량과 점점 더 흡사해진다.
차량은 각각 왼쪽/오른쪽 바퀴를 가지고 있으며, 각 바퀴의 속력을 설정해주어 구동시킨다.
마찬가지로 좌표계의 좌측 하단이 0, 0 이다. 우측 방향이 x+, 위쪽 방향이 y+.

자동차를  (300,300)로 이동하고, 그 주변에 도착하면 정차한 후,(맘대로)
        (425, 425)로 이동하고, 그 주변에 도착하면 정차한 후,
        (75, 75)로 복귀하도록 코드를 짜보자.
        제자리회전 금지 >_<

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

GOAL = [[300, 300], [425, 425], [75, 75]]


# 좌표계의 좌측 하단이 0, 0 이다. 우측 방향이 x+, 위쪽 방향이 y+
class Car:
    def __init__(self, initial_location):
        self.x, self.y = initial_location

        self.length = 15
        self.width = 10
        self.tread = 10
        self.wheel_radius = 1

        self.heading = 0
        self.right_wheel = 0
        self.left_wheel = 0

        self.trigger = 2
        self.goal = 0
        self.decision = False

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
        pygame.draw.circle(screen, GREEN, [75, 500 - 75], 10)
        pygame.draw.circle(screen, BLUE, [300, 500 - 300], 10)
        pygame.draw.circle(screen, BLUE, [425, 500 - 425], 10)

        a = atan2(self.width, self.length)
        b = sqrt(self.length ** 2 + self.width ** 2) / 2
        corner1 = [self.x + cos(self.heading - a) * b, 500 - (self.y + sin(self.heading - a) * b)]
        corner2 = [self.x + cos(self.heading + a) * b, 500 - (self.y + sin(self.heading + a) * b)]
        corner3 = [self.x + cos(self.heading + pi - a) * b, 500 - (self.y + sin(self.heading + pi - a) * b)]
        corner4 = [self.x + cos(self.heading + pi + a) * b, 500 - (self.y + sin(self.heading + pi + a) * b)]
        pygame.draw.polygon(screen, RED, [corner1, corner2, corner3, corner4])

    def set_motor_value(self, count):
        print(self.goal)

        if self.heading < (-pi / 2):
            self.heading = abs(self.heading) - (pi / 2)

        if self.goal == 3:
            self.right_wheel = 0
            self.left_wheel = 0

        else:
            if not self.decision:
                if GOAL[self.goal][0] > round(self.heading * (GOAL[self.goal][1] - self.x) + self.y):
                    self.right_wheel = 1.1
                    self.left_wheel = 1

                elif GOAL[self.goal][0] == round(self.heading * (GOAL[self.goal][1] - self.x) + self.y):
                    self.right_wheel = 1
                    self.left_wheel = 1

                elif GOAL[self.goal][0] < round(self.heading * (GOAL[self.goal][1] - self.x) + self.y):
                    self.right_wheel = 1
                    self.left_wheel = 1.1

                if abs(GOAL[self.goal][1] - round(self.y)) < 5:
                    self.decision = True
                    return
            else:
                print("goal")
                self.right_wheel = 0
                self.left_wheel = 0

                self.trigger += 1
                print(self.trigger)

                if self.trigger % 100 == 0:
                    self.decision = False
                    self.goal += 1
                    return

        print(round(self.x), round(self.y), self.heading)


def main():
    car = Car([75, 75])  # x, y
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

        pygame.display.flip()
        clock.tick(rate)
        count += 1


if __name__ == '__main__':
    main()
