# """""
# YD코딩세미나 - 6. 바둑판 출력
#
# a)
# 숫자 두개를 H,W 를 입력받고
# H의 세로길이와 W의 가로길이를 가진
# O로 초기화된 격자판을 출력
# ex)
# 3, 4
# OOOO
# OOOO
# OOOO
#
# b)
# (a) 의 격자판에서, h, w 로 위치를 입력해주면 해당좌표의 격자가 뒤집어짐(O -> X, X -> O)
# 모든 격자가 X가 되면 종료
# ex)
# 2, 1
# OOOO
# XOOO
# OOOO
#
# c)
# (a) 의 격자판에서, h, w 로 위치를 입력해주면 해당좌표와 위, 아래의 격자가 뒤집어짐(O -> X, X -> O)
# 모든 격자가 X가 되면 종료
# 힌트: 오버플로우/언더플로우의 뜻을 알고, 격자의 모서리에서 오버플로우와 언더플로우를 조심하자.
# ex)
# 2, 1
# XOOO
# XXOO
# XOOO
#
# 3,2
# XOOO
# XOOO
# OXXO
# """""
#
import copy

import numpy as np

h_H = 0
w_W = 0

def print_grid(grid):
    for h_idx in range(h_H):
        for w_idx in range(w_W):
            print(grid[h_idx][w_idx], end='')
        print('')

def game_a(h, w):
    grid = []
    w_grid = ['O'] * w
    for h_idx in range(h):
        grid.append(copy.deepcopy(w_grid))
    # grid = [w_grid for _ in range(h)]

    print_grid(grid)

    return grid

def game_b(grid, h, w):
    global h_H, w_W

    if grid[h - 1][w - 1] == 'X':
        grid[h - 1][w - 1] = 'O'
    else:
        grid[h - 1][w - 1] = 'X'

    print_grid(grid)

    # detect finish
    count = 0
    for h_idx in range(h_H):
        for w_idx in range(w_W):
            if grid[h_idx][w_idx] == 'X':
                count += 1
                if count == h_H * w_W:
                    return 'done'

def game_c(grid, h, w):
    global h_H, w_W

    # grid[h - 1][w - 1] 기준 / 하 grid[h][w - 1] / grid[h - 2][w - 1] 상 / grid[h - 1][w - 2] 좌 / grid[h - 1][w] 우

    # 기준
    if grid[h - 1][w - 1] == 'O':
        grid[h - 1][w - 1] = 'X'
    else:
        grid[h - 1][w - 1] = 'O'

    # 상
    if h > 1:
        if grid[h - 2][w - 1] == 'O':
            grid[h - 2][w - 1] = 'X'
        else:
            grid[h - 2][w - 1] = 'O'
    # 하
    try:
        if grid[h][w - 1] == 'O':
            grid[h][w - 1] = 'X'
        else:
            grid[h][w - 1] = 'O'
    except:
        pass
    # 좌
    if w > 1:
        if grid[h - 1][w - 2] == 'O':
            grid[h - 1][w - 2] = 'X'
        else:
            grid[h - 1][w - 2] = 'O'

    # 우
    try:
        if grid[h - 1][w] == 'O':
            grid[h - 1][w] = 'X'
        else:
            grid[h - 1][w] = 'O'
    except:
        pass

    print_grid(grid)

    # detect finish
    count = 0
    for h_idx in range(h_H):
        for w_idx in range(w_W):
            if grid[h_idx][w_idx] == 'X':
                count += 1
                if count == h_H * w_W:
                    return 'done'

def main():
    global h_H, w_W
    h_H, w_W = map(int, input('H, W를 입력하시오: ').split(','))
    grid = game_a(h_H, w_W)

    game_ver = input('(b), (c) 버전을 선택하시오: ')

    if game_ver == 'b':
        while True:
            h_g, w_g = map(int, input('H, W를 입력하시오: ').split(','))
            b = game_b(grid, h_g, w_g)
            if b == 'done':
                break

    elif game_ver == 'c':
        while True:
            h_g, w_g = map(int, input('H, W를 입력하시오: ').split(','))
            c = game_c(grid, h_g, w_g)
            if c == 'done':
                break


if __name__ == '__main__':
    main()
