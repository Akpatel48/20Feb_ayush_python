#Write a Python program to copy the contents of a file to another file
fil=open('txt1','w')
file=open('txt2','w')

fil.write(input("enter you write:"))
fil.close()
fil=open('txt1','r')

temp=fil.read()

file.write(temp)    #file copy in txt 2
file.close()
file=open('txt2','r')
print("file 2:",file.read())