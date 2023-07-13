# M 0
def count_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'M':
                new_matrix[i][j] = 'M'
            else:
                count = 0
                for dir in directions:
                    x, y = i + dir[0], j + dir[1]
                    if 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 'M':
                        count += 1
                new_matrix[i][j] = count

    return new_matrix



matrix = [
    [0, 'M', 0, 'M', 0],
    [0, 0, 'M', 0, 0],
    [0, 0, 0, 0, 0],
    ['M', 'M', 0, 0, 0],
    [0, 0, 0, 'M', 0]
]

result = count_matrix(matrix)

for row in result:
    print(row)
