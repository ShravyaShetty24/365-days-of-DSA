#Functional Recursion
#sum of n numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)
print(sum_n(2))


#Factorial of N numbers

#Parameterised

def fact(i,result):
    if i <= 1:
        print(result)
        return
    fact(i-1,result*i)
fact(4,1)

#Functional Recursion

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
print(fact(3))