def singlr_no(arr):
    map={}
    for i in range(len(arr)):
        if arr[i] in map:
            map[arr[i]]+=1
        else:
            map[arr[i]]=1
    for key,value in map.items():
        if value==1:
            return key
arr=[1,2,1,3,3,4,4,5,5]
print(singlr_no(arr))