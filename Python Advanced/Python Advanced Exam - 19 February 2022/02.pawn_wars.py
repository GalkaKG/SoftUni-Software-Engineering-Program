# 1-st decision

chessboard = []

for row in range(8, 0, -1):
    result = []
    for col in range(8):
        result.append(f'{chr(97 + col)}{row}')
    chessboard.append(result)

matrix = [input().split() for row in range(8)]

white_row, white_col, black_row, black_col = 0, 0, 0, 0

for idx, row in enumerate(matrix):
    if 'w' in row:
        white_row, white_col = idx, row.index('w')
    if 'b' in row:
        black_row, black_col = idx, row.index('b')

white_diagonals = [(-1, -1), (-1, +1)]
black_diagonals = [(+1, -1), (+1, +1)]

while True:
    if white_col != 0:
        if matrix[white_row - 1][white_col - 1] == 'b':
            print(f"Game over! White win, capture on {chessboard[white_row - 1][white_col - 1]}.")
            break
    if white_col != 7:
        if matrix[white_row - 1][white_col + 1] == 'b':
            print(f"Game over! White win, capture on {chessboard[white_row - 1][white_col + 1]}.")
            break

    matrix[white_row][white_col], matrix[white_row - 1][white_col] = '-', 'w'
    white_row -= 1

    if white_row == 0:
        print(f'Game over! White pawn is promoted to a queen at {chessboard[white_row][white_col]}.')
        break

    if black_col != 0:
        if matrix[black_row + 1][black_col - 1] == 'w':
            print(f"Game over! Black win, capture on {chessboard[black_row + 1][black_col - 1]}.")
            break
    if black_col != 7:
        if matrix[black_row + 1][black_col + 1] == 'w':
            print(f"Game over! Black win, capture on {chessboard[black_row + 1][black_col + 1]}.")
            break

    matrix[black_row][black_col], matrix[black_row + 1][black_col] = '-', 'b'
    black_row += 1

    if black_row == 7:
        print(f'Game over! Black pawn is promoted to a queen at {chessboard[black_row][black_col]}.')
        break





# 2-nd decision

def find_player_position(matrix, player):
    for row_index, row in enumerate(matrix):
        if player in row:
            return row_index, row.index(player)
    return None, None


def get_chess_position(row, col):
    chessboard = []

    for i in range(8, 0, - 1):
        letter = 96
        help_list = []
        for j in range(8):
            letter = letter + 1
            help_list.append(f'{chr(letter)}{i}')
        chessboard.append(help_list)
    return chessboard[row][col]


matrix = [input().split() for _ in range(8)]

current_player = 'w'
other_player = 'b'
current_player_position = find_player_position(matrix, 'w')
other_player_position = find_player_position(matrix, 'b')

current_delta = -1
other_delta = +1

is_queen = False
is_capture = False

while not is_queen and not is_capture:
    (current_player_row, current_player_col) = current_player_position
    (other_player_row, other_player_col) = other_player_position

    current_player_row += current_delta
    current_player_position = current_player_row, current_player_col

    if current_player_row == other_player_row and abs(current_player_col - other_player_col) == 1:
        is_capture = True
        current_player_position = current_player_row, other_player_col
    elif current_player_row in (0, 8 - 1):
        is_queen = True
    else:
        current_player_position, other_player_position = other_player_position, current_player_position
        current_delta, other_delta = other_delta, current_delta
        current_player, other_player = other_player, current_player

player = 'White' if current_player == 'w' else 'Black'
element = get_chess_position(*current_player_position)

if is_capture:
    print(f'Game over! {player} win, capture on {element}.')

if is_queen:
    print(f'Game over! {player} pawn is promoted to a queen at {element}.')
