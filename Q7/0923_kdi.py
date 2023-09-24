"""
주어진 함수 print_grid_map() 을 완성해보자.

print_grid_map()은 가상의 라이다 virtual_lidar() 로부터 1도의 간격으로 거리값이 담긴 길이 360개의 거리값을 배열로 받는다.
그 후, 10X10 그리드맵을 출력한다. 장애물(마우스)가 존재하는 좌표는 X로, 아닌 좌표는 O로 나타내어보자.

그리드맵의 실제크기는 500X500이며, 그리드맵의 중심에 라이다가 존재한다.
중심기준 오른쪽 수평직선에서 0도로 시작하고, 반시계 방향으로 359까지 증가한다.

단, print_grid_map() 에 인자로 주어진 sensor_data 의 값만 사용하자. 가공할 수 있는 값들은 sensor_data 의 360개의 값이 전부다.

"""

import pygame
from math import *
from pygame.locals import *
import sys
import numpy as np

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
rate = 90


def virtual_lidar(x, y):
    data_list = [0.0 for _ in range(360)]
    theta = atan2(y, x)
    degree_int = int(degrees(theta) + 0.5) % 360
    data_list[degree_int] = sqrt(x**2 + y**2)
    return data_list


def print_grid_map(sensor_data):
    grid_map = [['○ ' for _ in range(10)] for _ in range(10)]
    grid_map = np.array(grid_map)

    index_ans = np.nonzero(sensor_data)
    index = index_ans[0][0]
    x = sensor_data[index] * cos(radians(index)) + 250
    y = sensor_data[index] * sin(radians(index)) + 250

    index_y = int(9 - y // 50)
    index_x = int(x // 50)

    if 0 <= index_x < 10 and 0 <= index_y < 10:
        grid_map[index_y][index_x] = 'X '
    else:
        pass

    for i in range(grid_map.shape[-1]):
        for j in range(grid_map.shape[0]):
            print(grid_map[i][j], end='')
        print('')

    print('-' * 50)


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
