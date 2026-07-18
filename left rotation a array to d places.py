def left_rotation(arr,d):
    n=len(arr)
    d=d%n
    temp=arr[:d]
    for i in range(d,n):
        arr[i-d]=arr[i]
    for i in range(n-d,n):
        arr[i]=temp[i-(n-d)]
    return arr
n=int(input("enter the size of array:"))
arr=list(map(int,input("Enter the array elemts:").split()))
d=int(input("Enter the d:"))
print("Rotated arra:",left_rotation(arr,d))