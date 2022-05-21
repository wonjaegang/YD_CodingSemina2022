number = int(input('소수 판별할 숫자 입력(2 이상의 자연수) : '))


def verify_primenum(n):
    # 2를 입력받았을 때
    if n == 2:
        return 1

    # 3 이상 자연수 입력받았을 때
    for i in range(2, n):
        if n % i == 0:
            return 0
        return 1


if verify_primenum(number) == 1:
    print('%d은 소수입니다.' % number)
else:
    print('%d은 소수가 아닙니다.' % number)
