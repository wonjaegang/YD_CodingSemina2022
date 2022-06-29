H, W = map(int, input('원하는 H와 W의 크기를 각각 입력하시오').split(','))

# 원하는 열(H), 행(W)만큼 크기의 grid라는 H개의 리스트를 포함하는 다차원 배열 생성.

grid = [['O' for _ in range(W)] for _ in range(H)]

rows = len(grid)
cols = len(grid[0])

# 원하는 크기의 격자 출력

for r in range(rows):
    for c in range(cols):
        print(grid[r][c], end=" ")
    print()

# 원하는 좌표칸 뒤집기

while(1):
    h, w = map(int, input('뒤집을 격자판의 좌표(h, w)를 입력하시오').split(','))

    if grid[h-1][w-1] == 'O':
        grid[h-1][w-1] = 'X'
    else:
        grid[h-1][w-1] = 'O'

    for r in range(rows):
        for c in range(cols):
            print(grid[r][c], end=" ")
        print()

# 다 뒤집히면 게임 끝.

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                pass
            pass
        break

