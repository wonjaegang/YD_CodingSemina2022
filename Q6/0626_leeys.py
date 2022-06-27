def input_two_numbers():
    input_string = input().split(',')
    return list(map(lambda x: int(x), input_string))


def create_grid_by_input(input_array):
    grid = [['O' for width in range(input_array[1])] for height in range(input_array[0])]
    for i in grid:
        for j in i:
            print(j, end=" ")
        print()
    print()
    return grid


def reverse_grid_at_point(grid):
    while 1:
        input_array = input_two_numbers()
        if grid[input_array[0] - 1][input_array[1] - 1] == 'O':
            grid[input_array[0] - 1][input_array[1] - 1] = 'X'
        else:
            grid[input_array[0] - 1][input_array[1] - 1] = 'O'

        for i in grid:
            for j in i:
                print(j, end=' ')
            print()
        print()

        if grid == [['X' for width in range(len(grid[0]))] for height in range(len(grid))]:
            break


def reverse_grid_at_cross_shape(grid):
    while 1:
        input_array = input_two_numbers()
        center_point = [input_array[0] - 1, input_array[1] - 1]
        top_point = [input_array[0] - 2, input_array[1] - 1]
        bottom_point = [input_array[0], input_array[1] - 1]
        left_point = [input_array[0] - 1, input_array[1] - 2]
        right_point = [input_array[0] - 1, input_array[1]]

        for point in [center_point, top_point, bottom_point, left_point, right_point]:
            if 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid[0]):
                if grid[point[0]][point[1]] == 'O':
                    grid[point[0]][point[1]] = 'X'
                else:
                    grid[point[0]][point[1]] = 'O'

        for i in grid:
            for j in i:
                print(j, end=' ')
            print()
        print()

        if grid == [['X' for width in range(len(grid[0]))] for height in range(len(grid))]:
            break


def main():
    print("a) 격자의 Height, Width 입력")
    grid = create_grid_by_input(input_two_numbers())
    mode = input("모드 입력(b,c) : ")
    if mode == 'b':
        print("b) 뒤집을 격자의 좌표 입력(H, W)")
        reverse_grid_at_point(grid)
    else:
        print("b) 뒤집을 격자의 중심 좌표 입력(H, W)")
        reverse_grid_at_cross_shape(grid)


if __name__ == '__main__':
    main()
