def merge(arr):
    arr.sort()
    ans=[]
    for interval in arr:
        if not ans or interval[0]>ans[-1][1]:
            ans.append(interval)
        else:
            ans[-1][1]=max(ans[-1][1],interval[1])
    return ans
arr=[[1,3],[2,6],[8,10],[9,11],[15,18],[16,17],[2,4],[8,9]]
print(merge(arr))