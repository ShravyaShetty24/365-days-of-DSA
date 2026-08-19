def subarray(arr,x):
    prefix_sum=0
    cnt=0
    freq={0:1}
    for i in range(len(arr)):
        prefix_sum+=arr[i]
        remove=prefix_sum-x
        cnt+=freq.get(remove,0)
        freq[prefix_sum]=freq.get(prefix_sum,0)+1
    return cnt
arr=[1,2,3,-3,1,1,1,4,2,-3]
x=3
print(subarray(arr,x))