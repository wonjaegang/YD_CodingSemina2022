"""
BattleShip 게임을 만들어보자. 2인용 턴제 게임으로, 좌표를 통해 서로의 배를 격추시킨다. 모든 배를 먼저 격추시킨 플레이어가 승리한다.

특정 사이즈의 격자가 두 플레이어에게 동일하게 주어지고, 다양한 크기의 배를 두 플레이어가 각자 격자에 배치한다.
배는 세로, 또는 가로로 배치할 수 있다.
공격자가 특정좌표를 말하면, 수비자는 그 위치에 배가 있는지 없는지 말해준다.
공격자가 배가 차지하고있는 모든 좌표를 다 이야기했다면, 그 배는 격추된다.
모든 배를 격추시킨 플레이어가 승리한다.

각 문제는 모두 독립적인 문제.

각 플레이어에게 7X7 격자와, 길이가 2, 3, 4, 5이고 폭은 전부 1인 4척의 배가 주어진다.
플레이어1이 먼저 격자에 배를 배치한다. 배치를 입력받는 방법은 길이가 짧은 배 순으로, 배의 머리와 꼬리의 좌표를 입력한다.
(머리 행좌표, 머리 열좌표, 꼬리 행좌표, 꼬리 열좌표)
그 후 플레이어 2가 격자에 배를 배치한다.


a)
배치된 각 플레이어의 격자를 출력한다. 출력포맷 또한 자유롭게 구현해보자.


b)
플레이어1이 먼저 공격을 시작한다. 좌표(행, 열)를 입력하면, 프로그램은 자동으로 상대방 격자의 그 좌표에 배가 있는지 없는지 말해준다.
그 후, 플레이어 2가 공격을 진행한다.

각 공격이 진행된 후, 프로그램은 각 플레이어의 현재 격자상황을 출력해준다.
단, 배의 위치는 전부 숨긴채, 상대방이 공격한 격자의 위치와 그 위치에 배가 있었는지 없었는지만 보여준다.
출력 포맷은 자유롭게 구현해보자.

한 플레이어가 모든 배를 잃으면, 특정 플레이어가 승리했음을 출력하고 프로그램을 종료한다.



c)
GUI 로 구현해보자. pyGame 이나 tKinter 등을 사용해보자.



d)
플레이어 AI를 구현해보자.
자동으로 배를 배치하고, 공격한다.
깊게, 많이 고민해보자. 실제 구현은 하지 못하더라도, 아이디어를 여러개 생각해보자.


"""
import numpy as np

grid_map_a = np.array([['O  ' for _ in range(7)] for _ in range(7)])
grid_map_b = np.array([['O  ' for _ in range(7)] for _ in range(7)])

a_list = [[] for _ in range(4)]
b_list = [[] for _ in range(4)]

def creat_grid():
    grid = np.array([['O  ' for _ in range(7)] for _ in range(7)])
    return grid

def print_grid(grid):
    for row in range(grid.shape[-1]):
        for column in range(grid.shape[0]):
            print(grid[row][column], end='')
        print('')

def print_multi_grid(grid1, grid2):
    for row in range(grid1.shape[-1]):
        for column in range(grid1.shape[0]):
            print(f'{grid1[row][column]}', end='')
        print('             ', end='')
        for column in range(grid2.shape[0]):
            print(f'{grid2[row][column]}', end='')
        print('')

def input_two_points():
    input_string = input('배의 머리, 꼬리 좌표를 입력하시오: ').split(',')
    return list(map(lambda x : int(x), input_string))

def input_attack_points():
    input_attack_string = input('공격할 좌표를 입력하시오: ').split(',')
    return list(map(lambda x : int(x), input_attack_string))

def grid_battleship(grid):
    count = 0
    while count < 4:
        x1, y1, x2, y2 = input_two_points()
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1 - 1][i - 1] = 'X  '
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                grid[i - 1][y1 - 1] = 'X  '
        else:
            print('잘못된 배치입니다. 다시 입력하세요.')
            continue
        print_grid(grid)
        count += 1
    print('-' * 10)
    return grid

def attack_game_start(grid1, grid2):
    new_grid1 = creat_grid()
    new_grid2 = creat_grid()

    while True:
        count1 = 0
        count2 = 0
        print('플레이어1 공격하시오')
        x1, y1 = input_attack_points()
        if grid2[x1 - 1][y1 - 1] == 'X  ':
            print('플레이어1 공격 성공')
            grid2[x1 - 1][y1 - 1] = 'O  '
            new_grid2[x1 - 1][y1 - 1] = 'V  '
        else:
            print('플레이어1 공격 실패')

        print('플레이어2 공격하시오')
        x1, y1 = input_attack_points()
        if grid1[x1 - 1][y1 - 1] == 'X  ':
            print('플레이어2 공격 성공')
            grid1[x1 - 1][y1 - 1] = 'O  '
            new_grid1[x1 - 1][y1 - 1] = 'V  '
        else:
            print('플레이어2 공격 실패')

        # 1 or 2의 모든 좌표가 'O  ' 즉, 배가 모두 파괴되면 승자, 패자 결정.
        for element in grid2.flat:
            if element == 'X  ':
                count2 += 1
        if count2 == 0:
            print('플레이어1의 승리입니다.')
            break

        for element in grid1.flat:
            if element == 'X  ':
                count1 += 1
        if count1 == 0:
            print('플레이어2의 승리입니다.')
            break

        print('공격 결과')
        print_multi_grid(new_grid1, new_grid2)

def main():
    print('Player1, 자신의 배를 위치시키시오.')
    grid_p1 = grid_battleship(creat_grid())
    print('Player2, 자신의 배를 위치시키시오.')
    grid_p2 = grid_battleship(creat_grid())
    print('게임을 시작합니다. 각 플레이어는 공격할 좌표를 선정하여 공격하시오.')
    attack_game_start(grid_p1, grid_p2)
    print('게임 종료')


if __name__ == '__main__':
    main()