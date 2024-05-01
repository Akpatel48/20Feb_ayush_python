'''Write a Python program to check whether an element exists within a 
tuple.'''

no=int(input("enter no of element in tuple:"))
tupl=() #create truple
for i in range(no):
    data=input("enter values of tuple:")
    tupl+=(data,)

find=input("enter you find element:")

for i in tupl:
    if i==find:     #chek you finde number is exitsts or not
        print("element is exists")
    else:
        print("element are not exists")