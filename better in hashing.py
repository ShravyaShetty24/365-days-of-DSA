def single_no(arr):
    maxi=arr[0]
    for i in range(1,len(arr)):
        maxi=max(maxi,arr[i])
    hash_arr=[0]*(maxi+1)
    for i in range(len(arr)):
        hash_arr[arr[i]]+=1
    for i in range(len(arr)):
        if hash_arr[arr[i]]==1:
            return arr[i]
arr=[1,1,2,3,3,4,4]
print(single_no(arr))