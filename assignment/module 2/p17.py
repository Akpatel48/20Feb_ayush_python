'''Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string.'''
str1=input("enter first string:")   #inset string
str2=input("enter secand string:")  #inset string

e=str1[0]   
s=str1[1]
str1=s+e+str1[2:]   #swap first to characters

e=str2[0]   
s=str2[1]
str2=s+e+str2[2:]
print(f"{str1} {str2}")