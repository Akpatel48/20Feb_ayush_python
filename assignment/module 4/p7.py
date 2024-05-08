#Write a Python program to read a file line by line store it into a variable

fil=open('text','r')

re=fil.readlines()  

l1=re[0]    #file data store in variable
l2=re[1]    
print(l1)
print(l2)