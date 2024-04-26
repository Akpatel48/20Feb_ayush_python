'''Write a Python function that takes a list and returns a new list with unique 
elements of the first list.'''
list1=[]    #create list
unique=[]
def get():
    no=int(input("enter number of element get: "))
    for i in range(no):
        li=input("enter element values: ")
        list1.append(li)    #add data in list
def uni():
    for i in list1:
        if i not in unique:     #check value is unique or not
            unique.append(i)    
    print(unique)
get()
uni()
