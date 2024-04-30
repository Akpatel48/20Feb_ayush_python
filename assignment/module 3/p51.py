'''Write a Python function that checks whether a passed string is 
palindrome or not '''

string=input("enter string:")
temp=''
for i in range(len(string),0,-1):
    temp+=string[i-1]
if temp==string:
    print("string is not palindrome")
else:
    print("string is palindrom")
