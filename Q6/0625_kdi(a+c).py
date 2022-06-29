H, W = map(int, input('원하는 H와 W의 크기를 각각 입력하시오').split(','))

grid = [['O' for _ in range(W)] for _ in range(H)]

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        print(grid[r][c], end=" ")
    print()
