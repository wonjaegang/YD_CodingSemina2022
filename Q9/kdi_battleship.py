print("플레이어 1, 플레이어 2 각자 7X7 격자를 갖는다.")
import pygame

player1_grid = [['ㅡ' for _ in range(7)] for _ in range(7)]

for r in range(7):
    for c in range(7):
        print(player1_grid[r][c], end=" ")
    print()

print("플레이어 1의 턴입니다.")
for i in range(4):
    head_x, head_y, tail_x, tail_y = map(input('배의 머리 좌표, 꼬리 좌표 입력 (배의 길이 : %d)' % i+2).split(','))
