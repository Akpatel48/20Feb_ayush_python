#Write a Python program to count the number of lines in a text file. 

fil=open("txt.text",'r')

re=fil.readlines()
print("text file number of line:",len(re))  #get number of line in file