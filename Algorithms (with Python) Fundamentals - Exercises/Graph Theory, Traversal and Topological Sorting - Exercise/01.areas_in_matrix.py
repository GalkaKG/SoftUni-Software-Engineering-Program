def dfs(parent, row, col, matrix, visited):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    if visited[row][col]:
        return
    if matrix[row][col] != parent:
        return

    visited[row][col] = True
    dfs(parent, row - 1, col, matrix, visited)  # Up
    dfs(parent, row + 1, col, matrix, visited)  # Down
    dfs(parent, row, col - 1, matrix, visited)  # Left
    dfs(parent, row, col + 1, matrix, visited)  # Right


rows = int(input())
cols = int(input())

matrix = []
visited = []

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

areas = {}
total_areas = 0
for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        key = matrix[row][col]
        dfs(key, row, col, matrix, visited)
        if key not in areas:
            areas[key] = 1
        else:
            areas[key] += 1
        total_areas += 1

print(f'Areas: {total_areas}')
for area, size in sorted(areas.items()):
    print(f"Letter '{area}' -> {size}")
