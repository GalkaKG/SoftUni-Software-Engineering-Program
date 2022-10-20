# 1-st decision:

def get_magic_triangle(n):
    triangle = []
    for row in range(n):
        curr_nums = []
        idx = -1
        for col in range(row + 1):
            if col == 0:
                curr_nums.append(1)
            elif col == row:
                curr_nums.append(1)
            else:
                idx += 1
                num = triangle[row - 1][idx] + triangle[row - 1][idx + 1]
                curr_nums.append(num)
        triangle.append(curr_nums)
        
    return triangle




# 2-nd decision:

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
