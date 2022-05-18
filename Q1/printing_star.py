# 숫자를 입력받고 그만큼 별 트리 출력
# ex) 4
# ->
# *
# **
# ***
# ****


def print_star(num):
    for i in range(num):
        print('*' * (i + 1))


def main():
    input_num = int(input())
    print_star(input_num)


if __name__ == '__main__':
    main()
