n=int(input("Enter the size of an array:"))
arr=list(map(int,input("Enter the array elements:").split()))
mpp={}
for num in arr:
    if num in mpp:
        mpp[num]+=1
    else:
        mpp[num]=1
q=int(input("Enter the no. of queries:"))
while q>0:
    number=int(input("Enter no. to find frequency:"))
    print(mpp.get(number,0))
    q-=1