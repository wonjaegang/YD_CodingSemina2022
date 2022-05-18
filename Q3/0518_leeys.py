num = int(input("n번째 피보나치수(n 입력) : "))


def cal_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return cal_fibonacci(n - 1) + cal_fibonacci(n - 2)


print("%d번째 피보나치수 : %d" % (num, cal_fibonacci(num)))
