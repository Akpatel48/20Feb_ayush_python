'''Write a Python program to convert a list of characters into a string'''
list1=[]    #creat list
no=int(input("enter number of element: "))
def getdata():      #get data function
    for i in range(no):
        li=input("enter characters: ")
        list1.append(li)

def printdata():    #print data function
    x=''
    for i in list1:
        x+=i
    print(x)

getdata()   #call function
printdata() #call function