from collections import deque

seats = input().split(', ')
nums_line1 = deque([int(x) for x in input().split(', ')])
nums_line2 = [int(x) for x in input().split(', ')]

seats_matched = []
count_rotations = 0

while True:
    ascii_char_sum_nums = chr(nums_line1[0] + nums_line2[-1])
    seat_one = f'{nums_line1[0]}{ascii_char_sum_nums}'
    seat_two = f'{nums_line2[-1]}{ascii_char_sum_nums}'
    if seat_one in seats:
        seats_matched.append(seat_one)
        seats.remove(seat_one)
        nums_line1.popleft()
        nums_line2.pop()
    elif seat_two in seats:
        seats_matched.append(seat_two)
        seats.remove(seat_two)
        nums_line2.pop()
        nums_line1.popleft()
    else:
        nums_line1.rotate(-1)
        nums_line2 = nums_line2[-1:] + nums_line2[:-1]

    count_rotations += 1

    if len(seats_matched) == 3:
        break
    if count_rotations >= 10:
        break

print(f'Seat matches: {", ".join(seats_matched)}')
print(f'Rotations count: {count_rotations}')

