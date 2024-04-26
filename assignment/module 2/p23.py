'''Write a Python function to insert a string in the middle of a string'''

string=input("enter string:")   #get main string
string1=input("enter string add to middle:")    #get middel string

mids=len(string)//2 #lenth of sting
str=string[:mids]+string1+string[mids:]     #add string in middel
print(str)  #print new strig