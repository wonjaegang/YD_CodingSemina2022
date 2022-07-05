import pygame
from math import*
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
rate = 50


def virtual_lidar(x, y):
    data_list = [0.0 for _ in range(360)]
    theta = atan2(y, x)
    degree_int = int(degrees(theta) + 0.5) % 360
    data_list[degree_int] = sqrt(x**2 + y**2)
    return data_list


def print_grid_map(sensor_data):
    return 0


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        x = pygame.mouse.get_pos()[0] - 250
        y = -pygame.mouse.get_pos()[1] + 250

        sensor_data = virtual_lidar(x, y)
        print_grid_map(sensor_data)

        clock.tick(rate)


if __name__ == '__main__':
    main()
