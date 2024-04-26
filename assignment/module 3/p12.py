'''Write a Python program to convert a list of characters into a string'''
list1=[]    #creat list
no=int(input("enter number of element: "))
def getdata():  
    for i in range(no):
        li=input("enter characters: ")
        list1.append(li)

def printdata():
    x=''
    for i in list1:
        x+=i
    print(x)

getdata()
printdata()