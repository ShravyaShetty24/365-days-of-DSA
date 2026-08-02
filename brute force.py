def single_no(a):
    for i in range(len(a)):
        num=a[i]
        count=0
        for j in range(len(a)):
            if a[j]==num:
                count+=1
        if count==1:
            return num
a=[4,1,2,1,2]
print(single_no(a))