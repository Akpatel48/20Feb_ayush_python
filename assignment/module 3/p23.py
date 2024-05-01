#Write a Python program to find the length of a tuple. 

no=int(input("enter no of element in tuple:"))
tupl=()

for i in range(no):
    data=input("enter tuple value:")
    tupl+=(data,)

print(len(tupl))    #display truple lengthn