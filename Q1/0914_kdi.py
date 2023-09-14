# 숫자를 입력받고 그만큼 별 트리 출력
# ex) 4
# ->
# *
# **
# ***
# ****

def print_star(k):
    for i in range(k):
        print('*' * (i + 1))

def main():
    k = int(input('원하는 별 트리의 크기: '))
    print_star(k)

if __name__ == '__main__':
    main()
