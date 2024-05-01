#Write a Python program to append text to a file and display the text

file=open('text','a+')

wri=input("enter you write if file:")

file.write(wri)
file.close()
fil=open('text','r+')
re=fil.read()
print(re)