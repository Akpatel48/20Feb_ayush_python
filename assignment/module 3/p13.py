'''Write a Python program to select an item randomly from a list.'''
import random
list1=[]    #creat list
def get():
    no=int(input("enter number of element: "))
    for i in range(no):
        li=input("enter element values: ")
        list1.append(li)
    print(list1)
    print(f"randume values from list :{random.choice(list1)}")      #print list random 
get()

