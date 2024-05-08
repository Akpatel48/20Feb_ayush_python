#Write a Python program to map two lists into a dictionary 

list1=[]
list2=[]
dic={}
no=int(input("enter no of element in list:"))

for i in range(no):
    data=input("enter key:")
    list1.append(data)

for i in range(no):
    data=input("enter values:")
    list2.append(data)

for i in range(no):
    dic[list1[i]]=list2[i]  #  list to dic

print(f"list 1:{list1}")
print(f"list 2:{list2}")

print(f"after map dictionary:{dic}")    