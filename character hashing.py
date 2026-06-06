s=input("Enter string:")
hash_arr=[0]*26
for ch in s:
    hash_arr[ord(ch)-ord('a')]+=1
q=int(input("enter no. of queries:"))
while q>0:
    c=input("Enterr character:")
    print(hash_arr[ord(c)-ord('a')])
    q-=1