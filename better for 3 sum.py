def threesum(a):
    n=len(a)
    st=set()
    for i in range(n):
        hashset=set()
        for j in range(i+1,n):
            third= -(a[i]+a[j])
            if third in hashset:
                temp=[a[i],a[j],third]
                temp.sort()
                st.add(tuple(temp))
            hashset.add(a[j])
    return [list(x) for x in st]
a=[-1,0,1,2,-1,-4]
print(threesum(a))