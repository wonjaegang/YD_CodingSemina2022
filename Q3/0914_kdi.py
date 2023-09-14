# 정수 입력
# 입력한 정수 번 째 피보나치 수열 print

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def main():
    n = int(input('정수를 입력하시오: '))
    for i in range(n+1):
        if fibonacci(i) > 0:
            print(fibonacci(i), end=' ')

if __name__  == '__main__':
    main()
