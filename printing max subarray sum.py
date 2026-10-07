def max_subarray(arr):
    sum=0
    start=0
    ans_start=-1
    ans_end=-1
    max_len=float('-inf')
    for i in range(len(arr)):
        if sum == 0:
            start=i
        sum+=arr[i]
        if sum > max_len:
            max_len=sum
            ans_start=start
            ans_end=i
        if sum < 0:
            sum=0
    print("Maximum sum:",max_len)
    print("Maximum subarray:")
    for i in range(ans_start,ans_end+1):
        print(arr[i],end=" ")
arr=[-2,-3,4,-1,-2,1,5,-3]
max_subarray(arr)