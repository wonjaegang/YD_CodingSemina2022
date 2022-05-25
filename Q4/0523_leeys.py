boolean_state = [True, True, True, True, True]
state = ["On", "On", "On", "On", "On"]
switch_time = [0, 0, 0, 0, 0]


def initialization_by_input(n):     # 입력한 수에 따라 현재 state_bool 의 상태를 not state_bool 로 바꾸어 주는 함수
    if n != 0:
        boolean_state[n % 10 - 1] = not boolean_state[n % 10 - 1]
        initialization_by_input(n // 10)      # 재귀 함수 형태로 만들어 입력 받은 수의 각각의 자릿 수에 해당 하는 수를 인식


def boolean_state_to_state():       # True 와 False 로 표현된 boolean_state 를 On과 Off 로 이루어 진 state 로 변환 해주는 함수
    for i in range(5):
        if boolean_state[i]:
            state[i] = "On"
        else:
            state[i] = "Off"
            switch_time[i] += 1         # 점멸이 Off 가 된 순간 부터 시간 측정 시작


def main():
    minute = 0
    while True:
        minute += 1
        num = int(input("입력 - "))

        if num == 6:
            print("출력 - \"game over\"")
            break

        initialization_by_input(num)
        boolean_state_to_state()

        for i in range(5):                       # state 가 Off 가 된 후 5분이 지났을 때 다시 On 으로 바꿔 준다.
            if switch_time[i] % 5 == 0:          # Off 가 된 후 5분마다 판단
                if not boolean_state[i]:         # 점멸의 상태가 Off 인 것을 판단
                    boolean_state[i] = True      # Off 를 On 으로 변환
                    switch_time[i] = 0           # Off 였던 시간을 0으로 초기화

        print("출력 - %d분: 1:%s, 2:%s, 3:%s, 4:%s, 5:%s" % (minute, state[0], state[1], state[2], state[3], state[4]))


if __name__ == '__main__':
    main()
