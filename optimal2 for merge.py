def swapgreater(arr1,arr2,ind1,ind2):
    if arr1[ind1]>arr2[ind2]:
        arr1[ind1],arr2[ind2]=arr2[ind2],arr1[ind1]
def merge(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    length=n+m
    gap=(length//2)+(length%2)
    while gap>0:
        left=0
        right=left+gap
        while(right<length):
            if left<n and right>=n:
                swapgreater(arr1,arr2,left,right-n)
            elif left>=n:
                swapgreater(arr2,arr2,left-n,right-n)
            else:
                swapgreater(arr1,arr2,left,right)
            left+=1
            right+=1
        if gap==1:
            break
        else:
            gap=(gap//2)+(gap%2)
    return arr1,arr2
arr1=[1,3,5,7]
arr2=[0,2,6,8,9]
print(merge(arr1,arr2))