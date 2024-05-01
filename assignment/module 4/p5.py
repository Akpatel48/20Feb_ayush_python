#Write a Python program to read last n lines of a file. 

file=open('txt.text','r')

re=file.readlines()
li=re[-1]
print(li)