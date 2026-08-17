def subarray(arr,x):
    n=len(arr)
    cnt=0
    for i in range(n):
        for j in range(i,n):
            sum=0
            for k in range(i,j+1):
                sum+=arr[k]
            if sum==x:
                cnt+=1
    return cnt
arr=[1,2,3,-3,1,1,1,4,2,-3]
x=3
print(subarray(arr,x))