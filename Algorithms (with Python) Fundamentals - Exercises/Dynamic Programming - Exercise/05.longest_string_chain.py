from collections import deque

words = input().split()

size = [0] * len(words)
prev = [None] * len(words)

best_size = 0
best_idx = 0

for idx in range(len(words)):
    current_word = words[idx]
    current_size = 1
    parent = None

    for prev_idx in range(idx - 1, -1, -1):
        prev_word = words[prev_idx]

        if len(prev_word) >= len(current_word):
            continue

        if size[prev_idx] + 1 >= current_size:
            current_size = size[prev_idx] + 1
            parent = prev_idx

    size[idx] = current_size
    prev[idx] = parent

    if current_size > best_size:
        best_size = current_size
        best_idx = idx

lis = deque()

idx = best_idx
while idx is not None:
    lis.appendleft(words[idx])
    idx = prev[idx]

print(*lis, sep=' ')
