def next_permutation(arr):
    n=len(arr)
    indx=-1
    #find the breakpoint
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            indx=i
            break
    #if there is no breakpoint
    if indx==-1:
        arr.reverse()
        return arr
    #find the next greatest element
    for i in range(n-1,indx,-1):
        if arr[i]>arr[indx]:
            arr[i],arr[indx]=arr[indx],arr[i]
            break
    #reverse the suffix
    arr[indx+1:]=reversed(arr[indx+1:])
    return arr
arr=[2,1,5,4,3,0,0]
print(next_permutation(arr))