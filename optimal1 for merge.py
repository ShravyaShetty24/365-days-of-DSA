def merge2sorted(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    left=n-1
    right=0
    while left>=0 and right<m:
        if arr1[left] > arr2[right]:
            arr1[left],arr2[right]=arr2[right],arr1[left]
            left-=1
            right+=1
        else:
            break
    arr1.sort()
    arr2.sort()
arr1=[1,3,5,7]
arr2=[0,2,6,8,9]
merge2sorted(arr1,arr2)
print("arr1:",arr1)
print("arr2:",arr2)