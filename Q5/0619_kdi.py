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
import math

origin1, radius1, origin2, radius2 = map(int, input().split())
distance = math.sqrt((origin1-origin2)**2)  #원 중심 간의 거리

if radius1+radius2 == distance:
    print("외접")
elif abs(radius1-radius2) == distance:
    print("내접")
elif abs(radius1-radius2) < distance < radius1+radius2:
    print("교차")
elif abs(radius1-radius2) > distance:
    print("포함")
else:
    print("외부")
