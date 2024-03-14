#Write a Python program to get the Fibonacci series of given range.
no=int(input("enter number: "))
for i in range(1,no):
    i+=i
    print(i,end=" ")