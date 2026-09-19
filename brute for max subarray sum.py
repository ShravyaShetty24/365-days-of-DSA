def max_subarray(arr):
    n=len(arr)
    max_len=float('-inf')
    for i in range(n):
        for j in range(i,n):
            sum=0
            for k in range(i,j):
                sum+=arr[k]
            max_len=max(max_len,sum)
    return max_len
arr=[-2,-3,4,-1,-2,1,5,-3]
print(max_subarray(arr))