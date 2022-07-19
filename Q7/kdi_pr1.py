import math

grid_map = [['◯' for _ in range(10)] for _ in range(10)]

for degree in range(360):

    radian_num = math.radian(degree)
    radius = sensor_data[degree]
    x = math.cos(radian_num) * radius
    y = math.sin(radian_num) * radius

    if 0 < x <= 500 and 0 < y <= 500:
        if 0 < x <= 50:
            j = 0
        elif 50 < x <= 100:
            j = 1
        elif 100 < x <= 150:
            j = 2
        elif 150 < x <= 200:
            j = 3
        elif 200 < x <= 250:
            j = 4
        elif 250 < x <= 300:
            j = 5
        elif 300 < x <= 350:
            j = 6
        elif 350 < x <= 400:
            j = 7
        elif 400 < x <= 450:
            j = 8
        elif 450 < x <= 500:
            j = 9

        if 0 < y <= 50:
            i = 9
        elif 50 < y <= 100:
            i = 8
        elif 100 < y <= 150:
            i = 7
        elif 150 < y <= 200:
            i = 6
        elif 200 < y <= 250:
            i = 5
        elif 250 < y <= 300:
            i = 4
        elif 300 < y <= 350:
            i = 3
        elif 350 < y <= 400:
            i = 2
        elif 400 < y <= 450:
            i = 1
        elif 450 < y <= 500:
            i = 0
    grid_map[i][j] = 'X'

for row in range(10):
    for colomn in range(10):
        print(grid_map[row][colomn], end=" ")
    print()



