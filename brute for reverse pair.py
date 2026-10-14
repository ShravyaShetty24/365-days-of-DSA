def reversepair(a):
    n=len(a)
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if a[i]>2*a[j]:
                cnt+=1
    return cnt
a=[40,25,19,12,9,6,2]
print(reversepair(a))