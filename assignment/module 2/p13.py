'''Write a Python program to count the number of characters (character 
frequency) in a string '''
string=input("enter string:")   #get string
c=0
for i in string:
    if i!=' ':
        c=c+1
print(f"number of characters:{c}")  #print lenth of string