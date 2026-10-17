def binarysearch(arr,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif target>arr[mid]:
        return binarysearch(arr,mid+1,high,target)
    return binarysearch(arr,low,mid-1,target)
arr=[3,4,6,7,9,12,16,17]
n=8
target=7
low=0
high=n-1
print(binarysearch(arr,low,high,target))