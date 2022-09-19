def get_neighbors(matrix, row_bomb, col_bomb):
    neighbors = [
        [row_bomb - 1, col_bomb - 1],
        [row_bomb - 1, col_bomb],
        [row_bomb - 1, col_bomb + 1],
        [row_bomb, col_bomb - 1],
        [row_bomb, col_bomb + 1],
        [row_bomb + 1, col_bomb - 1],
        [row_bomb + 1, col_bomb],
        [row_bomb + 1, col_bomb + 1]
    ]

    valid = []
    for row, col in neighbors:
        if 0 <= row < len(matrix) and 0 <= col < len(matrix) and matrix[row][col] > 0:
            valid.append([row, col])
    return valid


size = int(input())

matrix = []

for r in range(size):
    matrix.append([int(x) for x in input().split()])

coordinates_of_the_bombs = input().split()

for bomb in coordinates_of_the_bombs:
    row_bomb, col_bomb = [int(x) for x in bomb.split(',')]

    explode_bomb = matrix[row_bomb][col_bomb]

    if explode_bomb <= 0:
        continue

    neighbors = get_neighbors(matrix, row_bomb, col_bomb)

    for r, c in neighbors:
        matrix[r][c] -= explode_bomb

    matrix[row_bomb][col_bomb] = 0

alive_cells = 0
sum_of_cells = 0
for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            sum_of_cells += el

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_cells}")
for row in matrix:
    print(*row)
