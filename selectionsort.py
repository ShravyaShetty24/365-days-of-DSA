def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
n=int(input("enter no. of element:"))
arr=[]
for i in range(n):
    arr.append(int(input()))
selection_sort(arr)
print("sorted array:")
for i in arr:
    print(i,end=" ") 