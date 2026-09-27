def merge2sorted(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    arr3=[0]*(n+m)
    left=0
    right=0
    index=0
    while left<n and right<m:
        if arr1[left]<=arr2[right]:
            arr3[index]=arr1[left]
            left+=1
            index+=1
        else:
            arr3[index]=arr2[right]
            right+=1
            index+=1
    while left<n:
        arr3[index]=arr1[left]
        left+=1
        index+=1
    while right<m:
        arr3[index]=arr2[right]
        right+=1
        index+=1
    for i in range(n+m):
        if i<n:
            arr1[i]=arr3[i]
        else:
            arr2[i-n]=arr3[i]
arr1=[1,3,5]
arr2=[2,4,6]
merge2sorted(arr1,arr2)
print("arr1:",arr1)
print("arr2:",arr2)