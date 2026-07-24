def intersection(a,b):
    i=0
    j=0
    ans=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            i+=1
        elif a[i]>b[j]:
            j+=1
        else:#if not ans or ans[-1]!=a[i]: this is for unique output
            ans.append(a[i])
            i+=1
            j+=1
    return ans
a=[1,2,2,3,4]
b=[2,2,3,5]
print(intersection(a,b))