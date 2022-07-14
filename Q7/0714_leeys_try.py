import pygame
from math import*
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
rate = 50


def virtual_lidar(x, y):
    data_list = [0.0 for _ in range(360)]
    theta = atan2(y, x)
    degree_int = int(degrees(theta) + 0.5) % 360
    data_list[degree_int] = sqrt(x**2 + y**2)
    return data_list


def print_grid_map(sensor_data, white, black):
    x_value = 0
    y_value = 0
    for index in range(len(sensor_data)):
        if sensor_data[index] != 0.0:
            theta = index
            x_value = sensor_data[index] * cos(radians(theta))
            y_value = sensor_data[index] * sin(radians(theta))
            break

    for i in range(-5, 5):
        for j in range(-5, 5):
            if i * 50 <= x_value < (i + 1) * 50 and j * 50 <= y_value < (j + 1) * 50:
                pygame.draw.rect(screen, white, [750 + i * 50, 250 - (j + 1) * 50, 50, 50])
            else:
                pygame.draw.rect(screen, black, [750 + i * 50, 250 - (j + 1) * 50, 50, 50])
                pygame.draw.rect(screen, white, [750 + i * 50, 250 - (j + 1) * 50, 50, 50], 1)
    return 0


def main():
    white = (255, 255, 255)
    black = (0, 0, 0)
    pygame.draw.circle(screen, white, [250, 250], 5)
    pygame.draw.line(screen, white, [500, 500], [500, 0])
    for grid_width in range(10):
        for grid_height in range(10):
            pygame.draw.rect(screen, white, [500 + 50 * grid_width, 50 * grid_height, 50, 50], 1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        x = pygame.mouse.get_pos()[0] - 250
        y = -pygame.mouse.get_pos()[1] + 250

        sensor_data = virtual_lidar(x, y)
        print_grid_map(sensor_data, white, black)

        pygame.display.flip()
        clock.tick(rate)


if __name__ == '__main__':
    main()
