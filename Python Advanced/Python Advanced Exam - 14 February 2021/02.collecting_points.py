def find_pos_player(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 'P':
                return row, col


size = int(input())
matrix = [input().split() for _ in range(size)]
command = input()

coins = 0
player_path = []
is_wall = False

while command:
    row, col = find_pos_player(matrix)
    positions = {
        'up': [row - 1, col],
        'down': [row + 1, col],
        'left': [row, col - 1],
        'right': [row, col + 1]
    }
    next_row, next_col = positions[command]

    if next_row >= size:
        next_row -= size
    if next_col >= size:
        next_col -= size

    if matrix[next_row][next_col] == 'X':
        if coins != 0:
            coins //= 2
        is_wall = True
        # break
    else:
        if matrix[next_row][next_col].isnumeric():
            coins += int(matrix[next_row][next_col])

    player_path.append([row, col])
    matrix[next_row][next_col] = 'P'
    matrix[row][col] = '0'

    if is_wall:
        break
    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break

    command = input()

last_rol, last_col = find_pos_player(matrix)
player_path.append([last_rol, last_col])

if coins < 100:
    print(f"Game over! You've collected {coins} coins.")

print('Your path:')
for path in player_path:
    print(path)
