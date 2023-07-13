#180 degrees
"""
def rotate_by180(matrix) :
    m = len(matrix)
    n = len(matrix[0])
    new_matrix = [[0]*n for i in range(m)]
    for i in range(m) :
        for j in range(n) :
            new_matrix[i][j] = matrix[m - i - 1][n - j - 1]
    return new_matrix

matrix = [[1 , 2 , 3],
          [4 , 5 , 6 ],
          [7 , 8 , 9]]

new = rotate_by180(matrix)
for row in new:
    print(row)
"""
#another solution
def rotate(lst) :

    for i in range(len(lst)):
        lst[i] = lst[i][::-1]
    return lst

lst = [[1, 2 , 3],
       [4 , 5, 6],
       [7 , 8 , 9]]
m = rotate(lst)
k = len(lst) - 1 
while k >= 0:
    print(lst[k])
    k -= 1


