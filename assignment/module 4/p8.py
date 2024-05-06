#Write a python program to find the longest words
list1= ["apple", "banana", "pear", "kiwi", "grapefruit", "watermelon"]
max=''
for i in list1:
    if len(max)<=len(i):
        max=i
print(max)