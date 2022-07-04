def create_grid():                                                                     # 격자 생성
    grid = [['X' for _ in range(7)] for _ in range(7)]
    return grid


def print_grid(grid):                                                                  # 격자 출력
    for i in grid:
        for j in i:
            if j == 6:
                print(j)
            else:
                print(j, end="  ")
        print()
    print()


def input_first_point_and_second_point():                                               # 머리 좌표와 꼬리 좌표 입력
    input_string = input("배치할 배의 머리 좌표, 꼬리 좌표 입력 : ").split(',')
    return list(map(lambda x: int(x), input_string))


def input_attack_point():                                                               # 공격할 좌표 입력
    input_string = input("공격할 좌표 입력 : ").split(',')
    return list(map(lambda x: int(x), input_string))


def put_the_battleship(grid):                                                           # 각각의 배를 배치
    repeat = 0
    while repeat < 4:
        x1, y1, x2, y2 = input_first_point_and_second_point()
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1 - 1][i - 1] = 'O'
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                grid[i - 1][y1 - 1] = 'O'
        else:
            print("잘못된 배치 입니다. 다시 입력해 주세요.\n")
            continue
        print_grid(grid)
        repeat += 1
    return grid


def simultaneous_print_of_two_gird(grid1, grid2):                                       # 두 개의 격자를 동시에 출력
    print("player 1                      player 2")
    for i in range(7):
        for j in range(7):
            print(grid1[i][j], end="  ")
        print("         ", end='')
        for j in range(7):
            print(grid2[i][j], end="  ")
        print()


def judge_of_success_or_failure_by_attack(grid1, grid2):                                # 공격의 성공 여부를 판단
    new_grid1 = create_grid()
    new_grid2 = create_grid()
    while True:
        print("player 1 의 공격 차례 입니다.")
        x1, y1 = input_attack_point()
        if grid2[x1 - 1][y1 - 1] == 'O':
            print("player 1 공격 성공!\n")
            grid2[x1 - 1][y1 - 1] = 'X'
            new_grid2[x1 - 1][y1 - 1] = 'O'
        else:
            print("player 1 공격 실패!\n")
            new_grid2[x1 - 1][y1 - 1] = 'O'

        print("player 2 의 공격 차례 입니다.")
        x2, y2 = input_attack_point()
        if grid1[x2 - 1][y2 - 1] == 'O':
            print("player 2 공격 성공!\n")
            grid1[x2 - 1][y2 - 1] = 'X'
            new_grid1[x2 - 1][y2 - 1] = 'O'
        else:
            print("player 2 공격 실패!\n")
            new_grid1[x2 - 1][y2 - 1] = 'O'

        simultaneous_print_of_two_gird(new_grid1, new_grid2)
        print("             (O : 공격을 시도한 좌표)\n")

        if grid1 == [['X' for _ in range(7)] for _ in range(7)]:
            print("player 2 의 승리")
            break
        elif grid2 == [['X' for _ in range(7)] for _ in range(7)]:
            print("player 1 의 승리")
            break


def main():
    print("player 1 차례 : 7 X 7 격자에 배 배치")
    grid_p1 = put_the_battleship(create_grid())
    print("player 2 차례 : 7 X 7 격자에 배 배치")
    grid_p2 = put_the_battleship(create_grid())
    print("배치 종료. 자신의 배치 재확인.")
    simultaneous_print_of_two_gird(grid_p1, grid_p2)
    print("\n상대의 배가 모두 함락될 때까지 게임이 진행 됩니다.\nplayer 1 부터 공격을 시작 합니다.")
    judge_of_success_or_failure_by_attack(grid_p1, grid_p2)
    print("게임 종료")


if __name__ == '__main__':
    main()
