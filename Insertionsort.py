def insertion_sort(arr):
    n=len(arr)
    for i in range(n-1):
        j=i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j=j-1
            print("Runs")#to check how many times it runs
n=int(input("enter no. of element:"))
arr=[]
for i in range(n):
    arr.append(int(input()))
insertion_sort(arr)
print("sorted array:")
for i in arr:
    print(i,end=" ") 