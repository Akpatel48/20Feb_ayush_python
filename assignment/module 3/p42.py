#Write a Python program to print all unique values in a dictionary.

no=int(input("enter number of element in list:"))
list1=[]
dic={}

for i in range(no):
    data=input("enter list value:")
    list1.append(data)

for i in range(no):
    if list1[i] not in dic.values():
        dic[i+1]=list1[i]
print(dic)