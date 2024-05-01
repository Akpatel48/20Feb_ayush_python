#Write a Python program to read a file line by line store it into a variable

fil=open('text','a')
no=int(input("enter number of lins in file enter:"))

for i in range(no):
    data=input(f"enter {i} line:")
    fil.write(f"{data}\n")
fil.close()
fil=open('text','r')

re=fil.readlines()

for i in re:
    
    print('v'+i)