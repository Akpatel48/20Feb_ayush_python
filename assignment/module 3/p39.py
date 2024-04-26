#Write a Python script to merge two Python dictionaries 

dict1={}
dict2={}

no=int(input("enter no of dictioaries pair:"))

for i in range(no):
    key=input("enter first key value:")
    value=input("enter first value")
    dict1[key]=value
for i in range(no):
    key=input("enter secend key value:")
    value=input("enter secend value")
    dict2[key]=value
dict1.update(dict2)
print(dict1)