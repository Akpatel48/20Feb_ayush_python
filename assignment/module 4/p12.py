#Write a Python program to copy the contents of a file to another file
fil=open('txt1','a')
file=open('txt2','a')

fil.write(input("enter you write:"))
fil.close()
fil=open('txt1','r')

temp=fil.read()

file.write(temp)
file.close()
file=open('txt2','r')
print("file 2:",file.read())