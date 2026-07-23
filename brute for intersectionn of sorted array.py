def intersection(a,b):
    ans=[]
    vis=[0]*len(b)
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j] and vis[j]==0:
                ans.append(a[i])
                vis[j]=1
                break
            if b[j]>a[i]:
                break
    return ans
a=[1,2,3,4,5]
b=[2,4,6,7]
print(intersection(a,b))