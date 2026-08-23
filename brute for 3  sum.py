def threesum(a):
    n=len(a)
    st=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if a[i]+a[j]+a[k]==0:
                    temp=[a[i],a[j],a[k]]
                    temp.sort()
                    st.add(tuple(temp))
    return [list(x) for x in st]
a=[-1,0,1,2,-1,-4]
print(threesum(a))