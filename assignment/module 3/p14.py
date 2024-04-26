'''Write a Python program to find the second smallest number in a list'''

list1=[]    #creat list
no=int(input("enter number of element: "))

for i in range(no):
    list1.append(int(input("enter values: ")))
print(list1)
small=0
for i in list1:
    if i<small:
        small=i
print(small)    #print small number 
