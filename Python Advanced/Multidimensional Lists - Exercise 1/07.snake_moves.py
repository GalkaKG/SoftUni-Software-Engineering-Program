rows, cols = [int(x) for x in input().split()]
word = input()

index = 0

for row in range(rows):
    elements = [None] * cols
    if row % 2 == 0:
        for col in range(cols):
            elements[col] = word[index % len(word)]
            index += 1
    else:
        for col in range(cols - 1, -1, -1):
            elements[col] = word[index % len(word)]
            index += 1

    print(''.join(elements))
