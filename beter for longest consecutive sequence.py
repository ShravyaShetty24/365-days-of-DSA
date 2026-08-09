def longest_consecutive(a):
    a.sort()
    longest=1
    cnt=0
    last_smaller=float('-inf')
    for i in range(len(a)):
        if a[i]-1 == last_smaller:
            cnt+=1
            last_smaller=a[i]
        elif a[i]!=last_smaller:
            cnt=1
            last_smaller=a[i]
        longest=max(longest,cnt)
    return longest
a=[100,102,100,101,101,4,3,2,3,2,1,1,1,2]
print(longest_consecutive(a))