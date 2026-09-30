def sign(arr):
    n=len(arr)
    pos=[]
    neg=[]
    for x in arr:
        if x>0:
            pos.append(x)
        else:
            neg.append(x)
    for i in range(n//2):
        arr[2*i]=pos[i]
        arr[2*i+1]=neg[i]
    return arr
arr=[3,1,-2,-5,2,-4]
print(sign(arr))