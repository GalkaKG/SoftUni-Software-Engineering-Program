def get_magic_triangle(n):
    result = []  # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]  for n = 5
    # 1 + n - x  - Formula
    for i in range(n):
        result.append([])
        result[i].append(1)
        for j in range(1, i):
            result[i].append(result[i - 1][j - 1] + result[i - 1][j])
        if i != 0:
            result[i].append(1)
    return result
