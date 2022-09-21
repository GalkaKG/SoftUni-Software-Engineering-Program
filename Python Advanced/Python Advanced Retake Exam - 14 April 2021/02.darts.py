def get_sum(matrix, row, col):
    sum_nums = 0
    for r in range(7):
        for c in range(7):
            if r == row and matrix[row][c].isnumeric():
                sum_nums += int(matrix[row][c])
            if c == col and matrix[r][col].isnumeric():
                sum_nums += int(matrix[r][col])
    return sum_nums


first_player_name, second_player_name = input().split(', ')
matrix = [input().split() for _ in range(7)]
coordinates = eval(input())

player1_score, player2_score = 501, 501
counter = 0
curr_player = 0
curr_player_name = ''
count1_turns = 0
count2_turns = 0
count_turns = 0
is_won = False

while coordinates:
    row, col = coordinates
    counter += 1
    if counter % 2 == 0:
        curr_player = player2_score
        curr_player_name = second_player_name
        count2_turns += 1
    else:
        curr_player = player1_score
        curr_player_name = first_player_name
        count1_turns += 1
    if row < 0 or row >= 7 or col < 0 or col >= 7:
        coordinates = eval(input())
        continue
    if matrix[row][col] == 'B':
        is_won = True
    elif matrix[row][col] == 'D':
        sum_nums = get_sum(matrix, row, col)
        sum_nums *= 2
        curr_player -= sum_nums
    elif matrix[row][col] == 'T':
        sum_nums = get_sum(matrix, row, col)
        sum_nums *= 3
        curr_player -= sum_nums

    elif matrix[row][col].isnumeric():
        curr_player -= int(matrix[row][col])

    if counter % 2 == 0:
        player2_score = curr_player
        count_turns = count2_turns
    else:
        player1_score = curr_player
        count_turns = count1_turns

    if curr_player <= 0:
        break
    if is_won:
        break
    coordinates = eval(input())

print(f"{curr_player_name} won the game with {count_turns} throws!")
