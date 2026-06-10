def partition(arr,low,high):
    p=arr[low]
    i=low
    j=high
    while i<j:
        while(arr[i]<=p and i<=high-1):
            i+=1
        while(arr[j]>p and j>=low+1):
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
def quick_sort(arr,low,high):
    if low<high:
        n=partition(arr,low,high)
        quick_sort(arr,low,n-1)
        quick_sort(arr,n+1,high)
def main(arr):
    quick_sort(arr,0,len(arr)-1)
    return arr
arr=[4, 6, 2, 5, 7, 9, 1, 3]
print(main(arr))