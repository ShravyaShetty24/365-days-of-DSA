def repmis(a):
    n=len(a)
    sn=(n*(n+1))//2
    s2n=(n*(n+1)*(2*n+1))//6
    s=0
    s2=0
    for i in range(0,n):
        s+=a[i]
        s2+=a[i]*a[i]
    val1=s-sn
    val2=s2-s2n
    val2=val2//val1
    x=(val1+val2)//2
    y=x-val1
    return x,y
a=[4,3,6,2,1,1]
print(repmis(a))