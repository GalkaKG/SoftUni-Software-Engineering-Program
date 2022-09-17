from collections import deque

words = deque(input().split())

primary_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

collected_colors = []

while words:
    left = words.popleft()
    right = words.pop() if words else ''

    result = left + right
    if result in primary_colors or result in secondary_colors:
        collected_colors.append(result)
        continue
    result = right + left
    if result in primary_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    left = left[:-1]
    right = right[:-1]

    if left:
        words.insert(len(words) // 2, left)
    if right:
        words.insert(len(words) // 2, right)

result = []

forming_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

for color in collected_colors:
    if color in primary_colors:
        result.append(color)
        continue

    is_collected = True
    for helper_color in forming_colors[color]:
        if helper_color not in collected_colors:
            is_collected = False
            break

    if is_collected:
        result.append(color)

print(result)
