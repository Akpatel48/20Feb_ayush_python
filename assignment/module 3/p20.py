#Write a Python program to create a tuple with numbers.

no=int(input("enter number of element in tuple:"))
tupl=()     #create truple
for i in range(no):
    data=int(input("enter tuple value:"))   #get truple values
    tupl+=(data,)   #add data in trupel
print(tupl)     #print truple