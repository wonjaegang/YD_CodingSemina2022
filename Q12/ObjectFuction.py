"""
목적함수를 계산하고 가장 작은 목적함수를 갖는 값을 찾아보자.

재원이는 기념일을 맞이해 여자친구에게 쫓을 선물하려한다.
하지만, 똑똑한 여자친구는 숫자에 굉장히 민감하여 자신이 좋아하는 수 만큼의 꽃을 받기를 원한다.
여자친구는 숫자를 볼 때 3가지의 취향에서 바라본다.
첫째, 그 수를 10으로 나눈 나머지가 클수록 그 수에대한 호감도가 내려간다.
둘째, 그 수가 50에 멀 수록 그 숫자에 대한 호감도가 내려간다.
셋째, 그 수가 짝수이면 그 숫자에 대한 호감도가 내려간다.

입력:

첫째 줄에 재원이가 선물하려는 꽃의 수들이 입력된다. (0 ~ 100의 정수)
둘째 줄에 여자친구에게 각 취향이 얼마나 중요한지 입력된다. (0와 1사이의 실수, 총 3개의 값)

출력:

여자친구의 취향을 고려했을 때, 재원이가 사야하는 꽃의 수를 골라 출력한다.

ex)
1 13 36 99 100
0.1 0.3 0.6
->
13

50 20 14 1 18 93 41
0.6 0.3 0.1
->
50

1 2 3 4 5 6 7
0 1 0
->
7

10 20 30 50 55 61 78 100
0.33 0.33 0.33
->
61
"""
