# X축 위에 원점이 있는 두 원이 있다.
# 각 원의 위치와 반지름을 통해 두 원 사이의 관계를 알아내고자한다.
# 난이도 별로 나눠진 a, b, c 출력을 순서대로 해결해보자.
#
# 입력: 1번 원의 원점의 x좌표, 반지름, 2번 원의 원점의 x좌표, 반지름을 순서대로 입력받는다.
#       단, 두 원의 원점의 위치는 같지 않으며, 각 좌표와 반지름의 길이는 자연수이다.
# 출력: a) 두 원사이의 관계를 외접/내접/교차/포함/외부 중 하나로 출력한다.(난이도 3)
#
#      b) 두 원의 접점의 x 좌표들을 담은 출력한다.
#         접점이 없다면 빈 배열을 출력한다.(난이도 6)
#
#      c) 두 원의 공통접선들의 기울기를 담은 배열을 출력한다.
#         공통접선이 없다면 빈 배열을 출력한다. 기울기가 무한대라면 inf 를 출력한다.(난이도 8)
#
# ex)
# 입력: 1, 1, 6, 4
#
# 출력: a) 외접
#      b) [2]
#      c) [0.75, -0.75, 'inf']

# ---------------------------------------------------------------------

# 함수 1
# 두 원의 원점과 반지름 입력 받기
# -> split 이라는 함수를 쓰면 ','으로 구분 하여 입력을 받는 게 가능 하구나
#   -> 이를 정수형 배열로 저장 하자.
#   -> 가독 하기 쉽게 변수를 각각 만들어 변수에 저장
#       -> 정적 변수로 할 수 없나? 불가능 하면 전역 변수로

# 함수 2
# 두 원의 관계 판단
# -> if 문을 이용
#   -> 각각의 조건을 달면 간단

# 함수 3
# 접점의 x 좌표를 출력
# -> 중첩 반복문 으로 모든 x 와 y 값을 대입 하여 성립 하는 점 찾기
#   -> 원의 방정식 을 이용 한다면?

# 함수 4
# 두 원의 공통 접선의 기울기 출력
# -> 접선의 방정식 공식을 이용 하여 함수 3 처럼 중첩 반복문 으로 찾으면 어떨까
#   -> 기울기 의 분모가 0일 때 if 문으로 inf 출력
sp1 = 0
r1 = 0
sp2 = 0
r2 = 0


def input_starting_point_and_radius():
    input_string = input().split(',')
    return list(map(lambda x: int(x), input_string))


def relation_of_circles(input_list):
    sp1 = input_list[0]         # starting point 1
    r1 = input_list[1]          # radius 1
    sp2 = input_list[2]         # starting point 2
    r2 = input_list[3]          # radius 2

    if sp1 + r1 < sp2 - r2 or sp2 + r2 < sp1 - r1:
        print("외부")
    elif sp1 + r1 == sp2 - r2 or sp2 + r2 == sp1 - r1:
        print("외접")
    elif (sp1 - r1 < sp2 - r2 and sp1 + r1 > sp2 + r2) or (sp2 - r2 < sp1 - r1 and sp2 + r2 > sp1 + r1):
        print("포함")
    elif sp1 - r1 == sp2 - r2 or sp1 + r1 == sp2 + r2:
        print("내접")
    else:
        print("교차")


def x_of_point_of_contact():
    for x1 in range(sp1 - r1, sp1 + r1 + 1):
        for y1 in range(r1 + 1):
            for x2 in range(sp2 - r2, sp2 + r2 + 1):
                for y2 in range(r2 + 1):
                    if pow(x1 - sp1, 2) + pow(y1, 2) == pow(r1, 2) and pow(x2 - r2, 2) + pow(y2, 2) == pow(r2, 2):
                        if x1 == x2 and y1 == y2:
                            print(str(x1))


def main():
    input_list = input_starting_point_and_radius()
    relation_of_circles(input_list)
    x_of_point_of_contact()


if __name__ == '__main__':
    main()
