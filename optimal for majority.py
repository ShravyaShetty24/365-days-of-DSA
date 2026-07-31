def majority(a):
    cnt=0
    for i in range(len(a)):
        if cnt==0:
            cnt=0
            ele=a[i]
        elif a[i]==ele:
            cnt+=1
        else:
            cnt-=1
    cnt1=0
    for i in range(len(a)):
        if a[i]==ele:
            cnt1+=1
    if cnt1 > len(a)//2:
        return ele
    return -1
a=[7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
print(majority(a))