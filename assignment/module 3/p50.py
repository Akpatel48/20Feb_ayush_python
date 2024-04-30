#Write a Python function to check whether a number is perfect or not. 

no=int(input("enter you check number is perfect or not:"))

def per():
    sum = 0
    
    for i in range(1,no):
    
        if(no%i == 0):
            sum += i
            
    if (sum == no):
        print(f"{no} is Perfect number")
    else:
        print(f"{no} is not perfect number")
            
per()