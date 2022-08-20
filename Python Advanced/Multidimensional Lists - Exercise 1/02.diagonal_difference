size = int(input())

matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split()])

primary = []
secondary = []
for i in range(size):
    primary.append(matrix[i][i])
    secondary.append(matrix[i][size - 1 - i])

primary_sum = sum(primary)
secondary_sum = sum(secondary)

print(abs(primary_sum - secondary_sum))
