#Write a Python script to merge two Python dictionaries 

dict1={}    #create dic
dict2={}    #create dic

no=int(input("enter no of dictioaries pair:"))  #get numberr of pire in dic

for i in range(no):
    key=input("enter first key value:")     #get key
    value=input("enter first value")        #get values
    dict1[key]=value    #inpute data in dic
for i in range(no):
    key=input("enter secend dic key value:")    #get key
    value=input("enter secend dic value")       #het value
    dict2[key]=value    #inpute data in secand dic
dict1.update(dict2)     #merge two dic
print(dict1)    