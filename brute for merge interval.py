def merge(arr):
    n=len(arr)
    arr.sort()
    ans=[]
    for i in range(n):
        start=arr[i][0]
        end=arr[i][1]
        if ans and end<=ans[-1][1]:
            continue
        for j in range(i+1,n):
            if arr[j][0]<=end:
                end=max(end,arr[j][1])
            else:
                break
        ans.append([start,end])
    return ans
arr=[[1,3],[2,6],[8,10],[9,11],[15,18],[16,17],[2,4],[8,9]]
print(merge(arr))