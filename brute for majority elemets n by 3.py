def majority(a,n):
    list=[]
    for i in range(len(a)):
        if len(list)==0 or list[0]!=a[i]:
            cnt=0
            for j in range(len(a)):
                if a[j]==a[i]:
                    cnt+=1
            if cnt>n//3:
                list.append(a[i])
        if len(list)==2:
            break
    return list
a=[1,1,1,3,3,2,2,2]
n=8
print(majority(a,n))