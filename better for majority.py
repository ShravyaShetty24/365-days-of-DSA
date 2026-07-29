def majority(a):
    freq={}
    for num in a:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    for key in freq:
        if freq[key]>len(a)//2:
            return freq[key]
    return -1
a=[2,2,3,3,1,2,2,]
print(majority(a))