# Write a Python program to find the repeated items of a tuple.

no=int(input("enter no of element tuple:"))     #tuple number of element
tupl=()     #create tuple
lis=[]      #create list
for i in range(no): 
    data=input("enter element value:")      #tuple values
    tupl+=(data,)
find=''
for i in tupl:
    if tupl.count(i)>1:     #chek item repeate or not
        lis.append(i)   
print("all repeated items",lis) 