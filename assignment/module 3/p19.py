'''Write a Python program to create a tuple with different data types.'''

list1=[]    #creat list

no=int(input("enter number of element:"))

for i in range(no):
    li=input("enter element values:")
    if li.isdigit():
        li=int(li)
    list1.append(li)
print(tuple(list1))     #print data in list to tuple