#Write a Python program to append text to a file and display the text

file=open('text','a+')  #open file

wri=input("enter you write if file:")   

file.write(wri)     #input file
file.close()    #close file
fil=open('text','r+')   #open file read mode
re=fil.read()   #read file
print(re)  