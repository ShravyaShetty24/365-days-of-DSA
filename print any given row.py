def print_row(n):
    ans=1
    print(ans,end=" ")
    for i in range(1,n):
        ans=ans*(n-i)
        ans=ans//i
        print(ans,end=" ")
n=5
print_row(n)