'''Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings.'''

str1=input("enter first string: ")  #get first dtring
str2=input("enter secand string: ")     #get secand string

print(f"first string lenth :{len(str1)}")   #print string len
print(f"secand string lenth :{len(str2)}")  #print string len

if str1[0]==str2[0] and str1[-1]==str2[-1]: #check list firste and lasat character are same or not
    print("string first and last character are same")
else:
    print("string first and last character are not same")
