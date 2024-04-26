#Write a Python program to get the Fibonacci series of given range.
no=int(input("enter number: "))     #input fibonnacci series range
#no+=1
a=1
b=0
for i in range(1,no+2):
    c=a+b
    a=b
    b=c
    print(b,end=" ")