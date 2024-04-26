'''Write a Python program that will return true if the two given integer 
values are equal or their sum or difference is 5.'''
a=int(input("enter number:"))   #input number
b=int(input("enter number:"))   #input number
temp=a+5
t=a-b
if a==b or a+b==5 or t==5:
    print("true")
else:
    print("false")