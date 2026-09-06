def generator(row):
    ans=1
    ansRow=[1]
    for col in range(1,row):
        ans=ans*(row-col)
        ans=ans//col
        ansRow.append(ans)
    return ansRow

def pascleTriangle(N):
    for i in range(1,N+1):
        print(*generator(i))
N=5
pascleTriangle(N)