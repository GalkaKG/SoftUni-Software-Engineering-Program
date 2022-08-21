rows, cols = [int(x) for x in input().split(', ')]
matrix = []
result = 0

for _ in range(rows):
    nums = [int(x) for x in input().split(', ')]
    result += sum(nums)
    matrix.append(nums)
    
print(result)
print(matrix)
