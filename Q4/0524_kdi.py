minute = 0

No_Jommel = {1:0, 2:0, 3:0, 4:0, 5:0}

while True:
    minute += 1
    number = int(input('점멸 빠진 사람의 번호를 입력하시오 : '))

    if number == 0:
        continue
    elif number == 6:
        break
    else:
        No_Jommel.get[number] = 5

    for key in No_Jommel:
        if No_Jommel[number] != 0:
            No_Jommel.get[number] -= 1

    if No_Jommel[number] = 0:
        state = "on"
    else
        state = "off"

    print("%d분 : 1:%s, 2:%s, 3:%s, 4:%s, 5:%s" %(minute)
