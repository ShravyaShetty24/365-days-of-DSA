def majority(a,n):
    list=[]
    map={}
    min=(n//3)+1
    for i in range(len(a)):
        map[a[i]]=map.get(a[i],0)+1
        if map[a[i]]==min:
            list.append(a[i])
        if len(list)==2:
            break
    return list
a=[1,1,1,1,3,2,2,2]
n=8
print(majority(a,n))