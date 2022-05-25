minute = 0

No_Jommel = [0, 0, 0, 0, 0]

while True:
    minute += 1
    number = int(input('점멸 빠진 사람의 번호를 입력하시오 : '))

    if number == 0:
        continue
    elif number == 6:
        break
    else:
        No_Jommel[number - 1] = 5

    for key in No_Jommel:
        if No_Jommel[number - 1] != 0:
            No_Jommel[number - 1] -= 1

    if No_Jommel[number] == 0:
        state = "on"
    else:
        state = "off"

    print("%d분 : 1:%s, 2:%s, 3:%s, 4:%s, 5:%s" %
          (minute, No_Jommel[0],  No_Jommel[1], No_Jommel[2], No_Jommel[3], No_Jommel[4]))
