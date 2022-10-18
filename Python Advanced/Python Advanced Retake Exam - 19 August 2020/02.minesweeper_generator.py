# 1-st decision:

def is_valid(row, col, SIZE):
    return 0 <= row < SIZE and 0 <= col < SIZE


def check_for_bombs_in_range(matrix, row, col):
    current_sum = 0
    for moving_row, moving_col in directions.values():
        check_row, check_col = row + moving_row, col + moving_col
        if is_valid(check_row, check_col, SIZE) and matrix[check_row][check_col] == '*':
            current_sum += 1
    matrix[row][col] = current_sum


SIZE = int(input())
bombs_number = int(input())

matrix = [list('0' * SIZE) for row in range(SIZE)]
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1),
              'top left diagonal': (-1, -1), 'top right diagonal': (-1, 1),
              'bottom left diagonal': (1, -1), 'bottom right diagonal': (1, 1)}

for bomb in range(bombs_number):
    bomb_row, bomb_col = [int(x) for x in input()[1:-1].split(', ')]
    matrix[bomb_row][bomb_col] = '*'


for row in range(SIZE):
    for col in range(SIZE):
        if matrix[row][col] != '*':
            check_for_bombs_in_range(matrix, row, col)

[print(*row) for row in matrix]






# 2-nd decision:

def is_inside(size, row, col):
    return 0 <= row < size and 0 <= col < size


def count_neighbour_bombs(matrix, row, col):
    count = 0
    if is_inside(size, row - 1, col) and matrix[row - 1][col] == '*':
        count += 1
    if is_inside(size, row + 1, col) and matrix[row + 1][col] == '*':
        count += 1
    if is_inside(size, row, col - 1) and matrix[row][col - 1] == '*':
        count += 1
    if is_inside(size, row, col + 1) and matrix[row][col + 1] == '*':
        count += 1
    if is_inside(size, row - 1, col - 1) and matrix[row - 1][col - 1] == '*':
        count += 1
    if is_inside(size, row + 1, col - 1) and matrix[row + 1][col - 1] == '*':
        count += 1
    if is_inside(size, row - 1, col + 1) and matrix[row - 1][col + 1] == '*':
        count += 1
    if is_inside(size, row + 1, col + 1) and matrix[row + 1][col + 1] == '*':
        count += 1
    return count


size = int(input())
bombs = int(input())

matrix = [list('0' * size) for _ in range(size)]

for _ in range(bombs):
    row, col = eval(input())
    matrix[row][col] = '*'

for row in range(size):
    for col in range(size):
        if matrix[row][col] == '*':
            continue
        cell_value = count_neighbour_bombs(matrix, row, col)
        matrix[row][col] = cell_value

for row in matrix:
    print(*row, sep=' ')
