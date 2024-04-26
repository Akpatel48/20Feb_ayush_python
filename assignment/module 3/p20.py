#Write a Python program to create a tuple with numbers.

no=int(input("enter number of element in tuple:"))
tupl=()
for i in range(no):
    data=int(input("enter tuple value:"))
    tupl+=(data,)
print(tupl)