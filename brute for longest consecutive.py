def longest_consecutive(a):
    longest=1
    for i in range(len(a)):
        x=a[i]
        cnt=1
        while(ls(a,x+1)==True):
            x=x+1
            cnt+=1
        longest=max(longest,cnt)
    return longest
def ls(a,num):
    for i in range(len(a)):
        if a[i]==num:
            return True
    return False
a=[102,4,100,1,101,3,2,1,1]
print(longest_consecutive(a))