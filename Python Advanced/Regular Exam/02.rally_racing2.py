def move_the_car(start_row, start_col, direction):
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    next_row, next_col = start_row + directions[direction][0], start_col + directions[direction][1]

    return next_row, next_col


N = int(input())
racing_number = input()

matrix = [input().split() for row in range(N)]

start_row, start_col = 0, 0
kilometres_passed = 0
finished = False
matrix[start_row][start_col] = 'C'

while not finished:
    direction = input()

    if direction == 'End':
        break

    next_row, next_col = move_the_car(start_row, start_col, direction)

    if matrix[next_row][next_col] == 'T':
        matrix[next_row][next_col] = '.'
        kilometres_passed += 30
        for idx, row in enumerate(matrix):
            if 'T' in row:
                next_row, next_col = idx, row.index('T')
    elif matrix[next_row][next_col] == 'F':
        finished = True
        kilometres_passed += 10
    elif matrix[next_row][next_col] == '.':
        kilometres_passed += 10

    matrix[next_row][next_col] = 'C'
    matrix[start_row][start_col] = '.'
    start_row, start_col = next_row, next_col

if finished:
    print(f"Racing car {racing_number} finished the stage!")
else:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {kilometres_passed} km.")
[print(''.join(row)) for row in matrix]
