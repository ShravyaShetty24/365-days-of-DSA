def foursum(num,target):
    num.sort()
    n=len(num)
    ans=[]
    for i in range(n-3):
        if i>0 and num[i]==num[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>i+1 and num[j]==num[j-1]:
                continue
            k=j+1
            l=n-1
            while k<l:
                total=num[i]+num[j]+num[k]+num[l]
                if total==target:
                    ans.append([num[i],num[j],num[k],num[l]])
                    k+=1
                    l-=1
                    while k<l and num[k]==num[k-1]:
                        k+=1
                    while k<l and num[l]==num[l+1]:
                        l-=1
                elif total<target:
                    k+=1
                else:
                    l-=1
    return ans
num=[1,1,1,2,2,2,3,3,3,4,4,4,5,5]
target=8
print(foursum(num,target))