# 정수 입력
# 입력한 정수가 소수 인지 아닌지 출력


def is_prime_number(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True


def main():
    input_num = int(input())
    print(is_prime_number(input_num))


if __name__ == '__main__':
    main()
