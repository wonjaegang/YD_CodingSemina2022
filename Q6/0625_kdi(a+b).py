H, W = map(int, input('원하는 H와 W의 크기를 각각 입력하시오').split(','))

grid = [['O' for _ in range(W)] for _ in range(H)]

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        print(grid[r][c], end=" ")
    print()

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

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                break

