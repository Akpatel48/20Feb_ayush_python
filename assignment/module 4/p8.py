#Write a python program to find the longest words

fil=open('text','r')

re=fil.readlines()
max=''
for i in re:
    print(len(i))
    if len(max)<=len(i):
        max+=i
       
print(max)