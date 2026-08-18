def subarray(arr,x):
    n=len(arr)
    cnt=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if sum==j:
                cnt+=1
    return cnt
arr=[1,2,3,-3,1,1,1,4,2,-3]
x=3
print(subarray(arr,x))