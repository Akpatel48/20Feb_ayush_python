#Write a Python program to check multiple keys exists in a dictionary

no=int(input("enter no of dictionary pair:"))
dic={}
lis=[]
for i in range(no):
    key=input("enter key value:")
    value=input("enter value:")
    dic[key]=dic


if len(dic.keys())<2:   #check multiple keys available or not
    print("NO")
else:
    print("YES")