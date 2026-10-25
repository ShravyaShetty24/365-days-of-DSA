def markrow(matrix,i,m):
    for j in range(m):
        if matrix[i][j]!=0:
            matrix[i][j]=-1
def markcol(matrix,j,n):
    for i in range(n):
        if matrix[i][j]!=0:
            matrix[i][j]=-1


def set_matrix(matrix):
    n=len(matrix)
    m=len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                markrow(matrix,i,m)
                markcol(matrix,j,n)
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==-1:
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