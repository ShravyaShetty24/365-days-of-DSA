def two_sum(arr,target):
    arr.sort()
    right=len(arr)-1
    left=0
    while(left<right):
        sum=arr[left]+arr[right]
        if sum==target:
            return "YES"
        elif sum<target:
            left+=1
        else:
            right-=1
    return "NO"
arr=[2,6,5,8,11]
target=14
print(two_sum(arr,target))