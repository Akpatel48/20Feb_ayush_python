#Write a Python program to read a file line by line and store it into a list

fil=open('txt.text','r')

re=fil.readlines()
list1=[]
for i in re:
    list1.append(i)
print(list1)