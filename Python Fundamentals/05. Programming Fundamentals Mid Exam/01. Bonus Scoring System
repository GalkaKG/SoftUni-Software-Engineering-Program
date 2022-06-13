from math import ceil
count_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
total_bonus = 0
max_bonus = 0
current_attendance = 0

for i in range(count_students):
    attendance = int(input())
    total_bonus = attendance / number_of_lectures * (5 + additional_bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        current_attendance = attendance

print(f'Max Bonus: {ceil(max_bonus)}.')
print(f'The student has attended {ceil(current_attendance)} lectures.')
