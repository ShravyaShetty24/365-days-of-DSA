def a_sign(arr):
    n=len(arr)
    pos=[]
    neg=[]
    for x in arr:
        if x > 0:
            pos.append(x)
        else:
            neg.append(x)
    if len(pos)>len(neg):
        for i in range(len(neg)):
            arr[2*i]=pos[i]
            arr[2*i+1]=neg[i]
        ind=len(neg)*2
        for i in range(len(neg),len(pos)):
            arr[ind]=pos[i]
            ind+=1
    else:
        for i in range(len(pos)):
            arr[2*i]=pos[i]
            arr[2*i+1]=neg[i]
        ind=len(pos)*2
        for i in range(len(pos),len(neg)):
            arr[ind]=neg[i]
            ind+=1
    return arr
arr=[-1,2,3,4,-3,1]
print(a_sign(arr))