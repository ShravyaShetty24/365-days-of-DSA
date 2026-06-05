n=int(input("enter size of array:"))
arr=list(map(int,input("Enter array elemetns:").split()))
hash_arr=[0]*13
for i in arr:
    hash_arr[i]+=1
q=int(input("Enter the no. of queries:"))
while q>0:
    number=int(input("Enter no. to find frequency:"))
    print(hash_arr[number])
    q-=1