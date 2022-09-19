def find_position(matrix):
    position_miner = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 's':
                position_miner = [row, col]
                break
    return position_miner


def moving_miner(matrix, row_miner, col_miner, command):
    positions = {
        'up': [row_miner - 1, col_miner],
        'down': [row_miner + 1, col_miner],
        'left': [row_miner, col_miner - 1],
        'right': [row_miner, col_miner + 1]
    }

    for k, v in positions.items():
        if command == k and 0 <= v[0] < len(matrix) and 0 <= v[1] < len(matrix):
            return v[0], v[1]
        # elif command == k and v[0] < 0 or v[0] >= len(matrix) or 0 > v[1] or v[1] >= len(matrix):
    return row_miner, col_miner


size = int(input())
commands = input().split()

matrix = []
for _ in range(size):
    matrix.append(input().split())

row, col = 0, 0
coals_total_count = 0

for r in matrix:
    for el in r:
        if el == 'c':
            coals_total_count += 1

for command in commands:
    row_miner, col_miner = find_position(matrix)
    row, col = moving_miner(matrix, row_miner, col_miner, command)

    if matrix[row][col] == 'e':
        print(f"Game over! ({row}, {col})")
        exit()
    elif matrix[row][col] == 'c':
        coals_total_count -= 1
        if coals_total_count == 0:
            print(f"You collected all coal! ({row}, {col})")
            exit()
        matrix[row][col] = 's'
        matrix[row_miner][col_miner] = '*'
    elif matrix[row][col] == '*':
        matrix[row][col] = 's'
        matrix[row_miner][col_miner] = '*'

print(f"{coals_total_count} pieces of coal left. ({row}, {col})")
