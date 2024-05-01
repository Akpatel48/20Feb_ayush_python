#Write a Python program to convert a tuple to a string.

no=int(input("enter number of element in tuple:"))

tupl=()
a=''
for i in range(no):
    data=input("enter tuple value:")
    tupl+=(data,)

for i in tupl:
    a+=i
print(a)    #display truple in string