def repmis(a):
    n=len(a)
    rep=-1
    miss=-1
    for i in range(1,n+1):
        cnt=0
        for j in range(n):
            if a[j]==i:
                cnt+=1
        if cnt==2:
            rep=i
        elif cnt==0:
            miss=i
    return rep,miss
a=[4,3,6,2,1,1]
print(repmis(a))