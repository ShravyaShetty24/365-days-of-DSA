def set_matrix(matrix):
    n=len(matrix)
    m=len(matrix[0])
    col=[0]*m
    row=[0]*n
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                row[i]=1
                col[j]=1
    for i in range(n):
        for j in range(m):
            if row[i]==1 or col[j]==1:
                matrix[i][j]=0
    return matrix
matrix=[
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1]
]
set_matrix(matrix)
for row in matrix:
    print(*row)