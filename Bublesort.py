def Buble_sort(arr):
    n=len(arr)
    didswap=0
    for i in range(n-1):
        
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                didswap=1
        if didswap==0:
            break
        print("runs")#to check how many times it runs
n=int(input("enter no. of element:"))
arr=[]
for i in range(n):
    arr.append(int(input()))
Buble_sort(arr)
print("sorted array:")
for i in arr:
    print(i,end=" ") 