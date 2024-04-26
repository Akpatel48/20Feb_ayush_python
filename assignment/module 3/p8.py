'''Write a Python program to check a list is empty or not'''
l=[]    #create list
size=int(input("enter number of element :"))
for i in range(size):
    li=input("enter element values :")
    l.append(li)
if len(l)!=0:   #check list is empty or not
    print("list is not empty")  
else:
    print("list is empty")