def get_next_pos(direction, row, col, steps):
    if direction == 'up':
        return row - steps, col
    if direction == 'down':
        return row + steps, col
    if direction == 'left':
        return row, col - steps
    if direction == 'right':
        return row, col + steps


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


size = 5
matrix = []

player_row = 0
player_col = 0
total_targets = 0

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == 'x':
            total_targets += 1
        elif row_elements[col] == 'A':
            player_row = row
            player_col = col

targets_left = total_targets
hit_targets = []

n = int(input())

for _ in range(n):
    command_args = input().split()
    command = command_args[0]
    direction = command_args[1]

    if command == 'move':
        steps = int(command_args[2])
        next_row, next_col = get_next_pos(direction, player_row, player_col, steps)

        if is_outside(next_row, next_col, size) or matrix[next_row][next_col] != '.':
            continue

        matrix[player_row][player_col] = '.'
        player_row, player_col = next_row, next_col
        matrix[player_row][player_col] = 'A'
    elif command == 'shoot':
        bullet_row, bullet_col = player_row, player_col
        while True:
            bullet_row, bullet_col = get_next_pos(direction, bullet_row, bullet_col, 1)

            if is_outside(bullet_row, bullet_col, size):
                break

            if matrix[bullet_row][bullet_col] == 'x':
                targets_left -= 1
                matrix[bullet_row][bullet_col] = '.'
                hit_targets.append([bullet_row, bullet_col])
                break

        if targets_left == 0:
            break

if targets_left == 0:
    print(f'Training completed! All {total_targets} targets hit.')
else:
    print(f'Training not completed! {targets_left} targets left.')

for hit_target in hit_targets:
    print(hit_target)
