#Write a Python program to read last n lines of a file. 

file=open('txt.text','r')   #open file

re=file.readlines()     #read file line
li=re[-1]   #get last line
print(li)