def countinversion(a):
    cnt=0
    n=len(a)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a[i]>a[j]:
                cnt+=1
    return cnt
a=[5,3,2,4,1]
print(countinversion(a))