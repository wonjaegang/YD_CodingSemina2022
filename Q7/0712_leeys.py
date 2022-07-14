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
    x_value = 0
    y_value = 0
    for index in range(len(sensor_data)):
        if sensor_data[index] != 0.0:
            theta = index
            x_value = sensor_data[index] * cos(radians(theta))
            y_value = sensor_data[index] * sin(radians(theta))
            break

    grid = [['O' for _ in range(10)] for _ in range(10)]
    for i in range(-5, 5):
        for j in range(-5, 5):
            if i * 50 <= x_value < (i + 1) * 50:
                if j * 50 <= y_value < (j + 1) * 50:
                    grid[abs(j - 4)][i + 5] = 'X'

    print()  # <- 이 print() 한 줄은 그냥 장식, 이게 조금(?) 눈이 더 편한 것 같아서

    for i in grid:
        for j in i:
            print(j, end='  ')
        print()
    return 0


def main():
    pygame.draw.circle(screen, (255, 255, 255), [250, 250], 5)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        x = pygame.mouse.get_pos()[0] - 250
        y = -pygame.mouse.get_pos()[1] + 250

        sensor_data = virtual_lidar(x, y)
        print_grid_map(sensor_data)

        pygame.display.flip()
        clock.tick(rate)


if __name__ == '__main__':
    main()
