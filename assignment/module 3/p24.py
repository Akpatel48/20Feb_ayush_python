#Write a Python program to convert a list to a tuple.

no=int(input("neter number of element in list:"))
lis=[]  #create list

for i in range(no):
    data=input("enter list element values:")
    lis.append(data)
print("tupel:",tuple(lis))   #display and convert list to tuple
print("list:",lis)