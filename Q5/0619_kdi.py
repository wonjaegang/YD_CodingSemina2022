# X축 위에 원점이 있는 두 원이 있다.
# 각 원의 위치와 반지름을 통해 두 원 사이의 관계를 알아내고자한다.
# 난이도 별로 나눠진 a, b, c 출력을 순서대로 해결해보자.
#
# 입력: 1번 원의 원점의 x좌표, 반지름, 2번 원의 원점의 x좌표, 반지름을 순서대로 입력받는다.
#       단, 두 원의 원점의 위치는 같지 않으며, 각 좌표와 반지름의 길이는 자연수이다.
# 출력: a) 두 원사이의 관계를 외접/내접/교차/포함/외부 중 하나로 출력한다.(난이도 3)
#
#      b) 두 원의 접점의 x 좌표들을 담은 배열을 출력한다.
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
import math

origin1, radius1, origin2, radius2 = map(int, input('원의 위치와 반지름을 각각 입력하시오').split())
distance = math.sqrt((origin1-origin2)**2)  #원 중심 간의 거리

if radius1+radius2 == distance:
    print("a) 외접\n")  # c 결과 ㅁ,ㅌ,inf

    # x 좌표 구하는 식
    if origin1 < origin2:
        x_point = origin1 + radius1
    else:
        x_point = origin2 + radius2
    print("b) [%d]\n" % x_point)

    # 공통접선 기울기 배열 출력
    slope = (abs(radius1-radius2))/(math.sqrt((origin1-origin2)**2+(radius1-radius2)**2))
    print("c) [%1.2f, %1.2f, 'inf']" % (slope, -slope))

elif abs(radius1-radius2) == distance:
    print("a) 내접")

    # x 좌표 구하는 식
    if radius1 > radius2:
        if origin1 > origin2:
            x_point = origin1 - radius1
        else:
            x_point = origin1 + radius1
    else:
        if origin2 > origin1:
            x_point = origin2 - radius2
        else:
            x_point = origin2 + radius2
    print("b) [%d]" % x_point)

    # 공통접선 기울기 배열 출력
    print("c) ['inf']")

elif abs(radius1-radius2) < distance < radius1+radius2:
    print("a) 교차")  # c 결과 ㅁ,ㅌ

    # x 좌표 구하는 식
    print("b) []")

    # 공통접선 기울기 배열 출력
    slope = (abs(radius1-radius2))/(math.sqrt((origin1-origin2)**2+(radius1-radius2)**2))
    print("c) [%1.2f, %1.2f]" % (slope, -slope))

elif abs(radius1-radius2) > distance:
    print("a) 포함")

    # x 좌표 구하는 식
    print("b) []")

    # 공통접선 기울기 배열 출력
    print("c) ['inf']")

else:
    print("a) 외부")  # c 결과 a,c,v,d

    # x 좌표 구하는 식
    print("b) []")

    # 공통접선 기울기 배열 출력
