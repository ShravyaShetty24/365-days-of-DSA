a=[1,0,3,4,0,6]
def move_zero(a):
   temp=[]
   for i in range(len(a)):
        if(a[i]!=0):
            temp.append(a[i])
   for i in range(len(temp)):
        a[i]=temp[i]
   for i in range(len(temp),len(a)):
        a[i]=0
   return a
print(move_zero(a))