from collections import deque

nums = [int(x) for x in input().split()]

size = [0] * len(nums)
size[0] = 1

parent = [None] * len(nums)

best_idx = 0
best_size = 1

for current in range(1, len(nums)):
    current_number = nums[current]
    current_best_size = 1
    current_parent = None

    for prev in range(current - 1, -1, -1):
        prev_number = nums[prev]

        if prev_number >= current_number:
            continue

        if size[prev] + 1 >= current_best_size:
            current_best_size = size[prev] + 1
            current_parent = prev

    size[current] = current_best_size
    parent[current] = current_parent

    if current_best_size > best_size:
        best_size = current_best_size
        best_idx = current

result = deque()

while best_idx is not None:
    result.appendleft(nums[best_idx])
    best_idx = parent[best_idx]

print(*result, sep=' ')
