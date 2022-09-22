def find_snake_position(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 'S':
                return row, col


def is_valid(matrix, next_row, next_col):
    if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix):
        return True

    
size = int(input())
matrix = [list(input()) for _ in range(size)]

direction = input()

counter_food = 0

while direction:
    row_snake, col_snake = find_snake_position(matrix)
    possible_directions = {
        'up': [row_snake - 1, col_snake],
        'down': [row_snake + 1, col_snake],
        'left': [row_snake, col_snake - 1],
        'right': [row_snake, col_snake + 1]
    }

    next_row, next_col = possible_directions[direction]
    if not is_valid(matrix, next_row, next_col):
        matrix[row_snake][col_snake] = '.'
        print('Game over!')
        break

    if matrix[next_row][next_col] == 'B' and is_valid(matrix, next_row, next_col):
        matrix[next_row][next_col] = 'S'
        matrix[row_snake][col_snake] = '.'
        for row in range(size):
            for col in range(size):
                if matrix[row][col] == 'B':
                    matrix[row][col] = 'S'
                    matrix[next_row][next_col] = '.'
                    break
        direction = input()
        continue

    elif matrix[next_row][next_col] == '*' and is_valid(matrix, next_row, next_col):
        counter_food += 1

    matrix[next_row][next_col] = 'S'
    matrix[row_snake][col_snake] = '.'
    if counter_food == 10:
        print("You won! You fed the snake.")
        break

    direction = input()

print(f'Food eaten: {counter_food}')
for row in matrix:
    print(''.join(row))
