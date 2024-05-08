#Write a Python program to read a file line by line and store it into a list

fil=open('txt.text','r')    #open file

re=fil.readlines()
list1=[]    
for i in re:
    list1.append(i) #file data store in variable
print(list1)