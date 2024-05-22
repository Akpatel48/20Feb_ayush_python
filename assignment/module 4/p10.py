#Write a Python program to count the frequency of word in a file.

fil=open('txt.text','r')    

re=fil.readlines(1) #read first line
count=1
word = input("Enter word to find it's Frequency : ")
if word in fil.read():
    count+=1
    print(f"{word} is {count} times in File.")
    
else:
    print("There is no such word in File.")