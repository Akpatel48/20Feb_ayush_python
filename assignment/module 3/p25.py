#Write a Python program to reverse a tuple. 

no=int(input("enter no of element in tupel:"))

tupl=()     #create tuple

for i in range(no):
    data=input("enter element value:")
    tupl+=(data,)
print(tupl)
print(tupl[::-1])   #display reverse tuple