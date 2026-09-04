def NCR(n,r):
    res=1
    for i in range(r):
        res=res*(n-i)
        res=res//(i+1)
    return res
n=5
r=3
print(NCR(n-1,r-1))