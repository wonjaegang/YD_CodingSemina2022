# X축 위에 원점이 있는 두 원이 있다.
# 각 원의 위치와 반지름을 통해 두 원 사이의 관계를 알아내고자한다.
# 난이도 별로 나눠진 a, b, c 출력을 순서대로 해결해보자.
#
# 입력: 1번 원의 원점의 x좌표, 반지름, 2번 원의 원점의 x좌표, 반지름을 순서대로 입력받는다.
#       단, 두 원의 원점의 위치는 같지 않으며, 각 좌표와 반지름의 길이는 자연수이다.
# 출력: a) 두 원 사이의 관계를 외접/내접/교차/포함/외부 중 하나로 출력한다.(난이도 3)
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

# 23.09.18, 15:21 ~ 16: 25

import math

bet_2o_dis = 0
rad_sum = 0
rad_sub = 0

x1, r1, x2, r2 = 0, 0, 0, 0

def detect_relation_cir(x1, r1, x2, r2):
    global bet_2o_dis, rad_sub, rad_sum

    bet_2o_dis = abs(x1 - x2)
    rad_sum = r1 + r2
    rad_sub = abs(r1 - r2)

    #외부
    if bet_2o_dis > rad_sum:
        return '외부'

    elif bet_2o_dis == rad_sum:
        return '외접'

    elif bet_2o_dis < rad_sum:
        if bet_2o_dis == rad_sub:
            return '내접'
        elif bet_2o_dis < rad_sub:
            return '포함'
        else:
            return '교차'

def print_cross_x(ans_a):
    global x1, r1, x2, r2

    if ans_a == '외접':
        if x1 > x2:
            return [x2 + r2]
        else:
            return [x1 + r1]
    elif ans_a == '내접':
        if r2 > r1:
            if x2 > x1:
                return [x1 - r1]
            else:
                return [x1 + r1]
        else:
            if x1 > x2:
                return [x2 - r2]
            else:
                return [x2 + r2]
    else:
        return []

def common_tangent(ans_a):
    global bet_2o_dis, rad_sub, rad_sum

    if ans_a == '내접':
        return ['inf']
    elif ans_a == '포함':
        return []
    else:
        a = math.tan(math.asin(rad_sub / bet_2o_dis))
        b = math.tan(math.asin(rad_sum / bet_2o_dis))
        if ans_a == '외접':
            return [a, -a, 'inf']
        else:
            return [a, -a, b, -b]

def main():
    global x1, r1, x2, r2
    x1, r1, x2, r2 = map(int, input('입력: ').split(', '))
    ans_a = detect_relation_cir(x1, r1, x2, r2)
    print('a)', ans_a)

    ans_b = print_cross_x(ans_a)
    print('b)', ans_b)

    ans_c = common_tangent(ans_a)
    print('c)', ans_c)



if __name__ == '__main__':
    main()