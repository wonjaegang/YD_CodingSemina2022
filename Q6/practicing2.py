player1_grid = [['□' for _ in range(7)] for _ in range(7)]


def make_ship_position():
    for i in range(4):
        head_x, head_y, tail_x, tail_y = map(int, input('배의 머리 좌표와 꼬리 좌표를 입력하시오. (배의 길이는 %d) : ' % (i+2)).split(','))

        if head_x == tail_x:
            if abs(tail_y - head_y) + 1 > i+2:
                make_ship_position()

            else:
                for i in range(abs(tail_y - head_y) + 1):
                    if tail_y > head_y:
                        player1_grid[head_x - 1][head_y - 1 + i] = '■'
                    else:
                        player1_grid[tail_x - 1][tail_y - 1 + i] = '■'

                for i in range(7):
                    for j in range(7):
                        print(player1_grid[i][j], end=" ")
                    print()

        elif head_y == tail_y:
            for i in range(abs(tail_x-head_x)+1):
                if tail_x > head_x:
                    player1_grid[head_x - 1 + i][head_y - 1] = '■'
                else:
                    player1_grid[tail_x - 1 + i][tail_y - 1] = '■'

            for i in range(7):
                for j in range(7):
                    print(player1_grid[i][j], end=" ")
                print()

        else:
            print('배는 가로, 세로 배치만 가능합니다.')


def main():
    print("플레이어 1의 턴입니다.")
    make_ship_position()


if __name__ == '__main__':
    main()
