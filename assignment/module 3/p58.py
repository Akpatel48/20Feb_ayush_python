#Write a Python program to read a random line from a file.
import random

with open('txt.text', 'r') as file:     #open file read mode
        lines=file.readlines()  #read lines
        num=len(lines)  #get number of lines if file
        random=random.randint(0,num - 1)        


print(f"Random line from the file : {lines[random]}")   #display random line