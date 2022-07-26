import re

text = input()
pattern = r'([\||#])([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'
food_info = re.finditer(pattern, text)
total_calories = 0
print_info = []

for info in food_info:
    name = info.group(2)
    expiration_date = info.group(3)
    calories = info.group(4)
    total_calories += int(calories)
    print_info.append(f'Item: {name}, Best before: {expiration_date}, Nutrition: {calories}')


print(f'You have food to last you for: {total_calories // 2000} days!')
[print(info) for info in print_info]
