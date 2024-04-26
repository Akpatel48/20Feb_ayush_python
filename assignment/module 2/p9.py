#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
a=int(input("enter number:"))   #inser number  
b=int(input("enter number:"))   #inser number
c=int(input("enter number:"))   #inser number
if a==b or b==c or a==c:    #check conditien number equal or not
    sum=0
else:
    sum=a+b+c
print(f"sum of three values:{sum}")