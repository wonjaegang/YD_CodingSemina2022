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





# 함수 1
# 두 원의 원점과 반지름 입력 받기
# -> split 이라는 함수를 쓰면 ','으로 구분 하여 입력을 받을 수 있구나
#   -> 이를 정수형 배열로 저장 하자.
#   -> 가독 하기 쉽게 변수를 각각 만들어 변수에 저장
#       -> 정적 변수로 할 수 없나?

# 함수 2
# 두 원의 관계 판단
# ->




def input_starting_point_and_radius():
    input_string = input().split(',')
    input_int = list(map(lambda x: int(x), input_string))

    starting_point_1 = input_int[0]
    radius_1 = input_int[1]
    starting_point_2 = input_int[2]
    radius_2 = input_int[3]


def relationship_of_circles(input)


def main():



if __name__ == '__main__':
    main()