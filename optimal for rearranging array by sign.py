def sign(arr):
    n=len(arr)
    ans=[0]*n
    posindx=0
    negindx=1
    for i in range(n):
        if arr[i]<0:
            ans[negindx]=arr[i]
            negindx+=2
        else:
            ans[posindx]=arr[i]
            posindx+=2
    return ans
arr=[3,1,-2,-5,2,-4]
print(sign(arr))