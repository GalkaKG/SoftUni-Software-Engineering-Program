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
