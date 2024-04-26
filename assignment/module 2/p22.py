'''Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string.'''

str1=input("enter string:")     #get string

if len(str1) <2:    #check string len
    print("instead of the emoty string")
else:
    str=str1[:2]+str1[-2:]      #first 2 and last 2 chars
    print(str)  #print first 2 and last 2 chars