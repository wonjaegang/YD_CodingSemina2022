# 재원이는 상대 팀의 점멸을 체크하는 프로그램을 구현중입니다.
# 상대팀은 1~5의 번호가 매겨져있습니다.
# 점멸체크는 1분마다 진행되고, 점멸은 5분 후에 돌아옵니다.
# 입력: 점멸이 빠진 상대방의 번호를 입력합니다.
#      동시에 여러명의 점멸이 빠질 수도 있습니다.
#      아무도 점멸이 빠지지 않았다면 0을 입력합니다.
#      6을 입력하면 프로그램을 종료합니다.
# 출력: 현재 상대팀원들의 점멸 On/Off 상태를 출력합니다.
#
# ex)
# 입력 - 1
# 출력 - 1분: 1:Off, 2:On, 3:On, 4:On, 5:On
# 입력 - 0
# 출력 - 2분: 1:Off, 2:On, 3:On, 4:On, 5:On
# 입력 - 23
# 출력 - 3분: 1:Off, 2:Off, 3:Off, 4:On, 5:On
# 입력 - 0
# 출력 - 4분: 1:Off, 2:Off, 3:Off, 4:On, 5:On
# 입력 - 0
# 출력 - 5분: 1:Off, 2:Off, 3:Off, 4:On, 5:On
# 입력 - 45
# 출력 - 6분: 1:On, 2:Off, 3:Off, 4:Off, 5:Off
# 입력 - 0
# 출력 - 7분: 1:On, 2:Off, 3:Off, 4:Off, 5:Off
# 입력 - 0
# 출력 - 8분: 1:On, 2:On, 3:On, 4:Off, 5:Off
# 입력 - 6
# 출력 - "game over"

flash_state = [0, 0, 0, 0, 0]


def string_input():
    # input_string = input()
    # k = []
    # for i in range(len(input_string)):
    #     k.append(int(input_string[i]))
    # return k

    # input_string = input()
    # k = []
    # for str_num in input_string:
    #     k.append(int(str_num))
    # return k

    input_string = input()
    if not int(input_string):
        return []
    else:
        return list(map(lambda x: int(x), input_string))


def update_flash_state(num_array):
    # for i in range(len(num_array)):
    #     flash_state[num_array[i - 1]] = 5

    for num in num_array:
        flash_state[num - 1] = 6

    # for i in range(len(flash_state)):
    #     if flash_state[i] != 0:
    #         flash_state[i] -= 1

    for i in range(len(flash_state)):
        if flash_state[i]:
            flash_state[i] -= 1


def print_state():
    print(flash_state)


def main():
    pass
    # 입력받기
    # -> 입력 -> (문자열->정수배열)
    # -> 0이나 6 분류
    # 입력을 받은선수의 상태 업데이트
    # 정수배열을 입력 -> 상태배열업데이트
    # -> 번호 Off, 루프마다 시간 -
    # 출력
    while True:
        num_array = string_input()
        update_flash_state(num_array)
        print_state()


if __name__ == '__main__':
    main()
