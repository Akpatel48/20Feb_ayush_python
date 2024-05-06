'''Write a Python function that checks whether a passed string is 
palindrome or not '''

string=input("enter string:")   #get string
temp=''
for i in range(len(string),0,-1):
    temp+=string[i-1]
if temp==string:    #check string is palindrome or not
    print("string is not palindrome")
else:
    print("string is palindrom")
