def palindrom(i,s,n):
    if i>=n//2:
        return True
    if(s[i]!=s[n-i-1]):
        return False
    return palindrom(i+1,s,n)
s=input("Enter string: ")
if palindrom(0,s,len(s)):
    print("palindrom")
else:
    print("not palindrome")