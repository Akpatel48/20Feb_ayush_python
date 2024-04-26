'''Write a Python function to reverses a string if its length is a multiple of 4'''

str1=input("enter sting:")  #get string

if len(str1) % 4==0:    #check len of string
    print(str1[::-1])   #print reverses string
else:
    print("sorry string ont multiple 4 ")     
