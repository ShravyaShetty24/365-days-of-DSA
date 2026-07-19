def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
def left_ritation(arr,d):
    n=len(arr)
    d=d%n
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
    return arr
n=int(input("enter the no. of element:"))
arr=list(map(int,input("Enter the array element:").split()))
d=int(input("Enter the value of d:"))
print(left_ritation(arr,d))