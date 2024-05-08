'''Write a Python function to calculate the factorial of a number (a 
nonnegative integer)'''

no=int(input("Enter Number to Find Factorial : "))

def factorial(no):
    fact = 1
    if no < 0:
        print("this number is negative")
    elif no>= 0:        
        for i in range(1,no+1):
            fact *= i 
        print(f"Factorial of {no} is : {fact}")     #factorial number
        
factorial(no)