import pygame
from math import*
from pygame.locals import *
from time import sleep

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

        # ↓ 여기서 부터 연석 추가 ↓
        self.course = 0
        self.min_velocity = 0.5
        self.max_velocity = 0.7
        # ↑     여기 까지       ↑

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
        if self.course == 3:
            self.left_wheel = 0
            self.right_wheel = 0
        else:
            if count > 10:
                for i in range(3):
                    if self.course == i and abs(GOAL[i][1] - self.x) <= 1 and abs(GOAL[i][0] - self.y) <= 1:
                        self.left_wheel = 0
                        self.right_wheel = 0
                        sleep(1)
                        self.course = i + 1
                    else:
                        pass

            angle_difference_abs = 0
            for i in range(3):
                if self.course == i:
                    angle_difference_abs = atan2(GOAL[i][0] - self.y, GOAL[i][1] - self.x)

            angle_difference_to_goal = angle_difference_abs - self.heading
            if abs(angle_difference_to_goal) > 0.5 * pi:
                velocity_change = self.max_velocity
            else:
                velocity_change = abs(angle_difference_to_goal) * \
                                  (self.max_velocity - self.min_velocity) / (0.5 * pi - 0) + self.min_velocity

            if 0 <= angle_difference_to_goal:
                self.left_wheel = self.min_velocity
                self.right_wheel = velocity_change
            else:
                self.left_wheel = velocity_change
                self.right_wheel = self.min_velocity


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
