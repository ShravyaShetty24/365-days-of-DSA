def majority(a,n):
    cnt1=0
    cnt2=0
    ele1=float('-inf')
    ele2=float('-inf')
    for i in range(len(a)):
        if cnt1==0 and a[i]!=ele2:
            cnt1=1
            ele1=a[i]
        elif cnt2==0 and a[i]!=ele1:
            cnt2=1
            ele2=a[i]
        elif ele1==a[i]:
            cnt1+=1
        elif ele2==a[i]:
            cnt2+=1
        else:
            cnt1-=1
            cnt2-=1
    list=[]
    cnt1=0
    cnt2=0
    for i in range(len(a)):
        if ele1==a[i]:
            cnt1+=1
        if ele2==a[i]:
            cnt2+=1
    mini=(n//3)+1
    if cnt1>=mini:
        list.append(ele1)
    if cnt2>=mini:
        list.append(ele2)
    list.sort()
    return list
a=[1,1,1,3,3,2,2,2]
n=8
print(majority(a,n))