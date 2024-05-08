'''Write a Python function that takes a list of w and returns the length
of the longest one.'''
no=int(input("enter number word:"))
word=[]
max=0
for i in range(no):
    get=input("enter word:")
    word.append(get)
for i in word:
    if len(i) > max:    #check logest word in list 
        max=len(i)
        maxword=[i]
print("longest word in string: ",maxword)   #print longest word in string