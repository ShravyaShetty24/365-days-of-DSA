def foursum(num,target):
    n=len(num)
    st=set()
    for i in range(0,n):
        for j in range(i+1,n):
            seen=set()
            for k in range(j+1,n):
                fourth=target-(num[i]+num[j]+num[k])
                if fourth in seen:
                    temp=[num[i],num[j],num[k],fourth]
                    temp.sort()
                    st.add(tuple(temp))
                seen.add(num[k])
    return [list(x) for x in st]
num=[1,2,-1,-2,2,0,-1]
target=0
print(foursum(num,target))