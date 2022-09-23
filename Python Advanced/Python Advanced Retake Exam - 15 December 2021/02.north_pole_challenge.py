def find_position(matrix):
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 'Y':
                return row, col


rows, cols = [int(x) for x in input().split(', ')]
matrix = [input().split() for _ in range(rows)]


def get_next_position(matrix, row, col, direction, steps, cols):
    path = {
        'up': [row - 1, col],
        'down': [row + 1, col],
        'left': [row, col - 1],
        'right': [row, col + 1]
    }
    next_row, next_col = path[direction]
    if next_row == len(matrix):
        next_row = next_row % len(matrix)
    if next_col == cols:
        next_col = next_col % cols
    if next_row < 0:
        next_row = len(matrix) - 1
    if next_col < 0:
        next_col = cols - 1
    return next_row, next_col


collected_items = {'Christmas decorations': 0,
                   'Gifts': 0,
                   'Cookies': 0
                   }

count_gifts = 0

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == 'D' or matrix[r][c] == 'G' or matrix[r][c] == 'C':
            count_gifts += 1

merry_christmas = False

while True:
    if merry_christmas:
        break
    command = input()

    if command == 'End':
        break
    direction, steps = command.split('-')
    steps = int(steps)
    row, col = find_position(matrix)

    while steps:
        next_row, next_col = get_next_position(matrix, row, col, direction, steps, cols)
        if matrix[next_row][next_col] == 'D':
            count_gifts -= 1
            collected_items['Christmas decorations'] += 1
        elif matrix[next_row][next_col] == 'G':
            count_gifts -= 1
            collected_items['Gifts'] += 1
        elif matrix[next_row][next_col] == 'C':
            count_gifts -= 1
            collected_items['Cookies'] += 1

        matrix[next_row][next_col] = 'Y'
        matrix[row][col] = 'x'
        row, col = next_row, next_col
        steps -= 1
        if count_gifts == 0:
            merry_christmas = True
            break

if merry_christmas:
    print('Merry Christmas!')

print("You've collected:")
for k, v in collected_items.items():
    print(f'- {v} {k}')
for r in matrix:
    print(' '.join(r))
