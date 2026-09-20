def max_subarray(arr):
    n=len(arr)
    max_len=float('-inf')
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            max_len=max(max_len,sum)
    return max_len
arr=[-2,-3,4,-1,-2,1,5,-3]
print(max_subarray(arr))