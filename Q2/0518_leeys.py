num = int(input("정수 입력 : "))
state = 1

for i in range(2, num):
    if num % i == 0:
        break
    else:
        state = 0

if state == 1:
    print("%d는 소수가 아닙니다." % num)
else:
    print("%d는 소수입니다." % num)
