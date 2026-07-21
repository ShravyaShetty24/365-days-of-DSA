def union_array(a,b):
    i=0
    j=0
    ans=[]
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            if not ans or ans[-1] != a[i]:
                ans.append(a[i])
            i+=1
        else:
            if not ans or ans[-1] != b[j]:
                ans.append(b[j])
            j+=1
    while i<len(a):
        if not ans or ans[-1] != a[i]:
            ans.append(a[i])
        i+=1
    while j<len(b):
        if not ans or ans[-1] != b[j]:
            ans.append(b[j])
        j+=1
    return ans
a=[1,2,3,3,4,5]
b=[5,7,8,9]
print(union_array(a,b))