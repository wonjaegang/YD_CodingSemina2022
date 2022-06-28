import math
global sp1
global sp2
global r1
global r2


def input_starting_point_and_radius():      # 두 원의 원점과 반지름 입력
    input_string = input("입력: ").split(',')
    print('')
    return list(map(lambda x: int(x), input_string))


def relation_of_circles(input_list):        # 두 원의 관계를 나타 내는 함수
    global sp1
    global sp2
    global r1
    global r2

    sp1 = input_list[0]         # starting point 1
    r1 = input_list[1]          # radius 1
    sp2 = input_list[2]         # starting point 2
    r2 = input_list[3]          # radius 2

    if sp1 + r1 < sp2 - r2 or sp2 + r2 < sp1 - r1:
        print("출력: a) 외부")
    elif sp1 + r1 == sp2 - r2 or sp2 + r2 == sp1 - r1:
        print("출력: a) 외접")
    elif (sp1 - r1 < sp2 - r2 and sp1 + r1 > sp2 + r2) or (sp2 - r2 < sp1 - r1 and sp2 + r2 > sp1 + r1):
        print("출력: a) 포함")
    elif sp1 - r1 == sp2 - r2 or sp1 + r1 == sp2 + r2:
        print("출력: a) 내접")
    else:
        print("출력: a) 교차")


def x_value_of_point_of_contact():      # 접점의 x 값을 구하는 함수
    if r1 + r2 < abs(sp1 - sp2):
        print("     b)", [])
    else:
        try:
            x_value = (sp1 ** 2 - sp2 ** 2 - (r1 ** 2 - r2 ** 2)) / (2 * (sp1 - sp2))
            print("     b)", [round(x_value, 2)])
        except ZeroDivisionError:
            print("     b)", [])


def slope_of_common_tangent_lines():    # 접선의 기울기 를 구하는 함수
    distance = abs(sp1 - sp2)
    if distance > r1 + r2:                              # 두 원의 관계가 외부일 때
        degree1 = math.asin((r1 + r2) / distance)
        slope1 = round(math.tan(degree1), 2)

        degree2 = math.asin(abs(r1 - r2) / distance)
        slope2 = round(math.tan(degree2), 2)

        print("     c)", [slope1, -slope1, slope2, -slope2])

    elif distance == r1 + r2:                           # 두 원의 관계가 외접일 때
        degree = math.asin(abs(r1 - r2) / distance)
        slope = round(math.tan(degree), 2)

        print("     c)", [slope, -slope, 'inf'])

    elif abs(r1 - r2) < distance < r1 + r2:             # 두 원의 관계가 교차일 때
        degree = math.asin(abs(r1 - r2) / distance)
        slope = round(math.tan(degree), 2)

        print("     c)", [slope, -slope])

    elif abs(r1 - r2) == distance:                      # 두 원의 관계가 내접일 때
        print("     c)", ['inf'])

    else:                                               # 두 원의 관계가 포함일 때
        print("     c)", [])


def main():
    input_list = input_starting_point_and_radius()
    relation_of_circles(input_list)
    x_value_of_point_of_contact()
    slope_of_common_tangent_lines()


if __name__ == '__main__':
    main()
