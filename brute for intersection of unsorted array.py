def intersection(a,b):
    s1=set(a)
    s2=set(b)
    return sorted(s1 & s2)
a=[4,3,2,6]
b=[2,5,3,4]
print(intersection(a,b))