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

# 2일, 약 5시간 걸림.

player_list = [0, 0, 0, 0, 0]
minute = 0

def detect_blackout_machine(team_num_list):
    # global boolean_list
    global minute
    global player_list
    minute += 1
    count = 0
    for index in team_num_list:
        # 입력 - 0
        if index == 0:
            for i in range(len(player_list)):
                if player_list[i] > 0:
                    player_list[i] += 1
                    if player_list[i] == 6:
                        player_list[i] = 0
        # 입력 - 6
        elif index == 6:
            return 'game over'
        # 입력 - 1~5
        else:
            player_list[index - 1] += 1
            if count == 0:
                for i in range(len(player_list)):
                    if i != (index - 1):
                        if player_list[i] > 0:
                            player_list[i] += 1
                            if player_list[i] == 6:
                                player_list[i] = 0
                count += 1

    copy_player_list = player_list.copy()

    for k in range(len(player_list)):
        if copy_player_list[k] != 0:
            copy_player_list[k] = 'Off'
        else:
            copy_player_list[k] = 'On'
    print(f'출력 - {minute}분: 1:{copy_player_list[0]}, 2:{copy_player_list[1]}, 3:{copy_player_list[2]}, 4:{copy_player_list[3]}, 5:{copy_player_list[4]}')


def main():
    while True:
        num_arr = []
        team_num = str(input('입력 - '))

        for i in range(len(team_num)):
            num_arr.append(int(team_num[i]))
        if detect_blackout_machine(num_arr) == 'game over':
            print('"game over"')
            break





if __name__ == '__main__':
    main()