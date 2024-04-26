'''Write a Python program to remove duplicates from a list'''
l=[]    #creat list
size=int(input("enter number of element :"))
for i in range(size):
    lis=input("enter element values :")
    l.append(lis)
l=set(l)
print(l)    #print after remove duplicates values