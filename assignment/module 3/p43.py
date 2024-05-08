#Why Do You Use the Zip () Method in Python?

no=int(input("enter number of element in list:"))
list1=[]
list2=[]

for i in range(no):
    data=input("enter first list value:")
    list1.append(data)
for i in range(no):
    data=input("enter secand list value:")
    list2.append(data)

lis=zip(list1,list2)    #zip list

print(list(lis))