ROWS = int(input())
matrix = [input().split() for _ in range(ROWS)]
COLS = len(matrix[0])
 
 
def is_safe(_matrix, row, col, visited):
    if (row >= 0) and (col >= 0) and (row < ROWS) and (col < COLS):
        if (matrix[row][col] == '.') and not visited[row][col]:
            return True
 
 
def depth_first_search(_matrix, row, col, visited, count):
    _rows = [-1, 0, 1, 0]
    _cols = [0, 1, 0, -1]
    visited[row][col] = True
 
    for i in range(4):
        if is_safe(_matrix, row + _rows[i], col + _cols[i], visited):
            count[0] += 1
            depth_first_search(_matrix, row + _rows[i], col + _cols[i], visited, count)
 
 
def largest_region(_matrix):
    visited = [[0] * COLS for _ in range(ROWS)]
    result = 0
 
    for i in range(ROWS):
        for j in range(COLS):
            if _matrix[i][j] == '.' and not visited[i][j]:
                count = [1]
                depth_first_search(_matrix, i, j, visited, count)
                result = max(result, count[0])
 
    return result
 
 
print(largest_region(matrix))
