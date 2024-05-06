'''Write a Python program to find the maximum and minimum numbers 
from the specified decimal numbers. '''

list1=[]
no=int(input("enter number of element in list:"))

for i in range(no):
    data=float(input("enter element values:"))
    list1.append(data)
max=max(list1)  #get max value  from list1
min=min(list1)  #get min value from list1

print(f"max value{max}")    #display max values
print(f"min value{min}")    #display min values