def threesumm(a):
    ans=[]
    n=len(a)
    a.sort()
    for i in range(n):
        if(i>0 and a[i]==a[i-1]):
            continue
        j=i+1
        k=n-1
        while j<k:
            summ=a[i]+a[j]+a[k]
            if summ<0:
                j+=1
            elif summ>0:
                k-=1
            else:
                temp=[a[i],a[j],a[k]]
                ans.append(temp)
                j+=1
                k-=1
                while(j<k and a[j]==a[j-1]):
                    j+=1
                while(j<k and a[k]==a[k+1]):
                    k-=1
    return ans
a=[-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
print(threesumm(a))