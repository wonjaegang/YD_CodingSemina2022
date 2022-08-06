import random

# 현대 모비스 입사생이 선물하려는 꽃의 수

flower_list = []
ran_flower = random.randint(0, 100)
ran_pick = random.randint(0, 100)

for i in range(ran_pick):
    while ran_flower in flower_list:
        ran_flower = random.randint(0, 100)
    flower_list.append(ran_flower)

print(*flower_list, sep=' ')

# 여자친구가 생각하는 취향 3개의 중요도

preference_list = []
ran_portion = round(random.random(), 1)

for j in range(3):
    preference_list.append(ran_portion)
    ran_portion = round(random.random(), 1)

print(*preference_list, sep=' ')

# 꽃의 수 중요도 계산

importance_num = 0
importance_list = []

for k in range(ran_pick):
    importance_num = (flower_list[k] % 10) * preference_list[0] + \
                     abs(flower_list[k] - 50) * preference_list[1] + \
                     abs((flower_list[k] % 2) - 1) * preference_list[2]
    importance_list.append(importance_num)

# importance_list 중 제일 작은 값 찾기 (importance_num 값이 작을수록 취향에 가깝다 : 값이 클수록 호감도가 낮다)

importance_want = importance_list[0]

for m in importance_list:
    if m < importance_want:
        importance_want = m

# importance_want의 인덱스를 찾고 그에 해당하는 flower_list 원하는 꽃의 개수 구하기

print('->')
print(flower_list[importance_list.index(importance_want)])
