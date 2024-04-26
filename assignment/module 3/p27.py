# Write a Python program to find the repeated items of a tuple.

no=int(input("enter no of element tuple:"))
tupl=()
lis=[]
for i in range(no):
    data=input("enter element value:")
    tupl+=(data,)
find=''
for i in tupl:
    if tupl.count(i)>1:
        lis.append(i)
print("all repeated items",lis)