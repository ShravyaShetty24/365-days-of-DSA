def two_sum(n,arr,target):
    map={}
    for i in range(n):
        a=arr[i]
        more=target-a
        if more in map:
            return "YES"  #return [map[more],i]
        map[a]=i
    return "NO"  #[-1,-1]
arr=[2,6,5,8,11]
target=14
print(two_sum(len(arr),arr,target))