#Write a Python program to write a list to a file

fil=open('text1','a')   #open file
no=int(input("enter number of element in list:"))
list1=[]
for i in range(no):
    data=input("enter list value:")
    list1.append(data)
a=list1
for i in list1:
    fil.write(f"{i}\n") #list write in file

fil.close() #close file
fil=open('text1','r')   #file open read mode
print("read file")
print(fil.read())