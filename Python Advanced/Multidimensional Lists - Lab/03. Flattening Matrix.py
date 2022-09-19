# first decision:

num = int(input())

matrix = [[int(y) for y in input().split(', ')] for x in range(num)]
flatted = [x for y in matrix for x in y]

print(flatted)




# second decision:

rows = int(input())
result = []

for _ in range(rows):
    nums = [int(x) for x in input().split(', ')]
    result.extend(nums)
print(result)
