def is_valid(row, col):
    return 0 <= row < 8 and 0 <= col < 8


def moves(row, col, direction, directions):
    row, col = row + directions[direction][0], col + directions[direction][1]
    return row, col


matrix = [input().split() for _ in range(8)]

king_row, king_col, queens_position = 0, 0, []

directions = {
    "up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1), "top left diagonal": (-1, -1),
    "top right diagonal": (-1, 1), "bottom left diagonal": (1, -1), "bottom right diagonal": (1, 1)
}

for row in range(8):
    if 'K' in matrix[row]:
        king_row, king_col = row, matrix[row].index('K')

for direction in directions:
    new_row, new_col = king_row, king_col
    for step in range(8):
        new_row, new_col = moves(new_row, new_col, direction, directions)
        if not is_valid(new_row, new_col):
            break
        if matrix[new_row][new_col] == 'Q':
            queens_position.append([new_row, new_col])
            break

if queens_position:
    [print(row) for row in queens_position]
else:
    print("The king is safe!")
