H, W = map(int, input('원하는 H와 W의 크기를 각각 입력하시오').split(','))

# 빈 리스트 a 생성
a = []

# a 안에 W만큼의 Row 'O'를 입력해줌
for j in range(W):
    a.append("O")

# 원하는 크기의 가로길이 (Row)만큼 생성된 a 리스트를 Var_1, Var_2... Var_H 원하는 (Column)개수 만큼의 a를 가지는 리스트 생성
for i in range(1, H+1):
    globals()['Var_{}'.format(i)] = a

# b라는 2차원 리스트를 만들기 위해 Var_1, Var_2 ... Var_H 를 넣음
for k in range(1, H+1):
    b = [(globals()['Var_{}'.format(k)])]

print(b)

"""""
for k in range(1, H+1):
    b = [globals()[k]]

print(b)
"""
"""
for k in range(1, H+1):
    print(''.join(globals()['Var_{}'.format(k)]))
"""

h, w = map(int, input('뒤집고 싶은 좌표(h, w)를 입력하시오').split(','))

if (Var_(h)[w]) == 'O':
    Var_(h)[w] = 'X'

for k in range(1, H+1):
    print(''.join(globals()['Var_{}'.format(k)]))
