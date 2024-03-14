'''Write a Python program that will return true if the two given integer 
values are equal or their sum or difference is 5.'''
a=int(input("enter number:"))
b=int(input("enter number:"))
temp=a+5
t=a-5
if a==b or a+b==5 or temp==b or t==b:
    print("true")