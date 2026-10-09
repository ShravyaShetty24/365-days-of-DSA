def repmis(a):
    n=len(a)
    freq=[0]*(n+1)
    for num in a:
        freq[num]+=1
    rep=-1
    miss=-1
    for i in range(1,n+1):
        if freq[i]==2:
            rep=i
        elif freq[i]==0:
            miss=i
    return rep,miss
a=[4,3,6,2,1,1]
print(repmis(a))