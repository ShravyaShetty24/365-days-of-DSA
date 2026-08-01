num=[1,1,0,1,1,1,0,1,1]
def max_consecutive(num):
    maxi=0
    count=0
    for i in range(len(num)):
        if num[i]==1:
            count+=1
            maxi=max(maxi,count)
        else:
            count=0
    return maxi
print(max_consecutive(num))