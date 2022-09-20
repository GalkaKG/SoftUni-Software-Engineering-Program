def find_position(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == 'E':
                return r, c


def move_func(matrix, command, row, col):
    positions = {
        'up': [row - 1, col],
        'down': [row + 1, col],
        'left': [row, col - 1],
        'right': [row, col + 1]
    }

    new_row, new_col = positions[command]
    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix):
        return new_row, new_col
    else:
        if command == 'up':
            return 5, col
        elif command == 'down':
            return 0, col
        elif command == 'left':
            return row, 5
        elif command == 'right':
            return row, 0


matrix = [input().split() for _ in range(6)]
commands = input().split(', ')

dict_with_deposits = {'W': 0, 'M': 0, 'C': 0}

for command in commands:
    star_row, start_col = find_position(matrix)
    row, col = move_func(matrix, command, star_row, start_col)
    matrix[star_row][start_col] = '-'

    if matrix[row][col] == 'W':
        dict_with_deposits['W'] += 1
        print(f"Water deposit found at ({row}, {col})")
    elif matrix[row][col] == 'M':
        dict_with_deposits['M'] += 1
        print(f"Metal deposit found at ({row}, {col})")
    elif matrix[row][col] == 'C':
        dict_with_deposits['C'] += 1
        print(f"Concrete deposit found at ({row}, {col})")
    elif matrix[row][col] == 'R':
        print(f"Rover got broken at ({row}, {col})")
        break
    elif matrix[row][col] == '-':
        pass
    matrix[row][col] = 'E'

if dict_with_deposits['W'] > 0 and dict_with_deposits['M'] > 0 and dict_with_deposits['C'] > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
