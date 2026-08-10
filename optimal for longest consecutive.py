def longest_consecutive(a):
    n=len(a)
    if n==0:
        return 0
    longest=1
    st=set(a)
    for num in st:
        if num-1 not in st:
            cnt=1
            x=num
            while x+1 in st:
                x+=1
                cnt+=1
            longest=max(longest,cnt)
    return longest
a=[102,4,100,1,101,3,2,1,1]
print(longest_consecutive(a))