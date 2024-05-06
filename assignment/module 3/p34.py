#Write a Python script to check if a given key already exists in a dictionary.

dic={'id':1,'name':'ayush','age':19}

key=input("enter you finde key:")   #get find key

if key in dic:      #check key avelebe or not in dic
    print("\nkey are exists in dictionary")
else:
    print("\nkey are not exists in dictionary")