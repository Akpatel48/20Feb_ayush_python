#Write a Python program to check if a number is positive, negative or zero.
no=int(input("enter number: "))     #input number
if no>0:    #check condition
    print("positive")   #print massage
elif no<0:  
    print("negative")
else:
    print("zero")