def max_subarray(arr):
    sum=0
    max_len=float('-inf')
    for i in range(len(arr)):
        sum+=arr[i]
        if sum>max_len:
            max_len=sum
        if sum<0:
            sum=0
    if max_len<0:
        return 0
    return max_len
arr=[-2,-3,4,-1,-2,1,5,-3]
print(max_subarray(arr))