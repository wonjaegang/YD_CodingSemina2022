number = int(input('\'n번째 피보나치 수열\' n 입력 : '))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("%d번째 피보나치 수열의 값 : %d" % (number, fibonacci(number)))
