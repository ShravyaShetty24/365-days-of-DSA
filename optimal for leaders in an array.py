def leaders_arr(a):
    n=len(a)
    maxi=float('-inf')
    ans=[]
    for i in range(n-1,-1,-1):
        if a[i]>maxi:
            ans.append(a[i])
        maxi=max(maxi,a[i])
    ans.sort()
    return ans
a=[10,22,12,3,0,6]
print(leaders_arr(a))