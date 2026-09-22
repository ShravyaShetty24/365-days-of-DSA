def foursum(num,target):
    n=len(num)
    st=set()
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    sum=num[i]+num[j]
                    sum+=num[k]
                    sum+=num[l]
                    if sum==target:
                        temp=[num[i],num[j],num[k],num[l]]
                        temp.sort()
                        st.add(tuple(temp))
    return [list(x) for x in st]
num=[1,0,-1,0,-2,2]
target=0
print(foursum(num,target))