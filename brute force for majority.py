def majority(a):
    n=len(a)
    for i in range(n):
        count=0
        for j in range(n):
            if a[i]==a[j]:
                count+=1
        if count>n//2:
            return count
    return -1
a=[2,2,1,1,1,2,2]
print(majority(a))