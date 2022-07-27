import re


def calculate_points(destinations):
    total_points = 0
    destination_names = []

    for destination in destinations:
        total_points += len(destination.group(2))
        destination_names.append(destination.group(2))
    return total_points, ', '.join(destination_names)


text = input()

pattern = r'([=|/])([A-Z][A-Za-z]{2,})\1'
valids = re.finditer(pattern, text)
points, names = calculate_points(valids)
print(f'Destinations: {names}')
print(f'Travel Points: {points}')
