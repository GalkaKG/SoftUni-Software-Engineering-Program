def get_position(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == 'P':
                return r, c


def get_next_position(matrix, row, col):
    positions = {
        'up': [row - 1, col],
        'down': [row + 1, col],
        'left': [row, col - 1],
        'right': [row, col + 1]
    }
    next_row, next_col = positions[command]
    return next_row, next_col


text = input()
size = int(input())
matrix = [input().split() for _ in range(size)]
matrix2 = []
for row in matrix:
    for el in row:
        help_list = []
        for el2 in el:
            help_list.append(el2)
        matrix2.append(help_list)
matrix = matrix2
n = int(input())

result_stack = []
for el in text:
    result_stack.append(el)

for i in range(n):
    command = input()
    row, col = get_position(matrix)
    next_row, next_col = get_next_position(matrix, row, col)

    if next_row < 0 or next_row >= size or next_col < 0 or next_col >= size and result_stack:
        result_stack.pop()
    else:
        if matrix[next_row][next_col].isalpha():
            result_stack.append(matrix[next_row][next_col])
        matrix[next_row][next_col] = 'P'
        matrix[row][col] = '-'

print("".join(result_stack))
for r in matrix:
    print(''.join(r))
