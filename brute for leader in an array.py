def leader_arr(a):
    ans=[]
    for i in range(len(a)):
        leader=True
        for j in range(i+1,len(a)):
            if a[j]>a[i]:
                leader=False
                break
        if leader==True:
            ans.append(a[i])
    return ans
a=[10,22,12,3,0,6]
print(leader_arr(a))