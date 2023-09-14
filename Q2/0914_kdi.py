# 정수 입력
# 입력한 정수가 소수 인지 아닌지 출력

def detect_prime(n):
    if n == 2:
        return 1

    if n >= 3:
        for i in range(2, n):
            if n % i == 0:
                return 0
            return 1

def main():
    n = int(input('정수 입력하시오: '))
    if detect_prime(n) == 1:
        print(f'{n}은 소수입니다.')
    else:
        print(f'{n}은 소수가 아닙니다.')


if __name__ == '__main__':
    main()