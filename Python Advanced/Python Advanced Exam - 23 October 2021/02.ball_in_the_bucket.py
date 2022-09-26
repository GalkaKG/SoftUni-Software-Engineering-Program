def is_valid(row, col):
    if 0 <= row < 6 and 0 <= col < 6:
        return True


matrix = [[int(x) if x.isdigit() else x for x in input().split()] for x in range(6)]
points = 0

for _ in range(3):
    row, col = eval(input())

    if is_valid(row, col) and matrix[row][col] == 'B':
        matrix[row][col] = 0
        for r in range(6):
            points += matrix[r][col]

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
else:
    if 100 <= points <= 199:
        prize = 'Football'
    elif points <= 299:
        prize = 'Teddy Bear'
    elif points >= 300:
        prize = 'Lego Construction Set'
    print(f"Good job! You scored {points} points, and you've won {prize}.")
