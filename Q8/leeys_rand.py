import pygame
from math import*
from pygame.locals import *
import random

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
        self.velocity = 3

    def set_steer(self, count):
        if 20 <= self.x <= 480 and 20 <= self.y <= 480:
            if not count % 30:
                self.direction = random.uniform(0, 2 * pi)
        else:
            self.direction += pi

    def Lidar(self):
        pass


def main():
    car = Car([250, 100])
    obstacle = Obstacle([250, 250], [50, 10])
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
