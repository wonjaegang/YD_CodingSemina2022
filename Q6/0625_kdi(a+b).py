#   a) 격자판 입력 및 출력
"""""
H, W = map(int, input('원하는 H와 W의 크기를 각각 입력하시오').split())
for i in range(H):
    for j in range(W):
        print("O", end='')
    print()

h, w = map(int, input('뒤집을 격자판의 좌표(h, w)를 입력하시오').split())

"""
H, W = map(int, input('원하는 H와 W의 크기를 각각 입력하시오').split())

a = []

for j in range(W):
    a.append("O")

for i in range(H):
    for k in a:
        print(k, end='')
    print()
