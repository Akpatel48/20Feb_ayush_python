#When will the else part of try-except-else be executed?


"""When will the else part of try-except-else be executed?

      - In Try-Except-Else else part will be executed if try part will get execute without any exception.
      - If any Exception occurs then else part will be not executed.
Example : Enter Numbers for Division"""
a = int(input("enter first number:"))
b = int(input("enter first number:"))

try:
    c = a/b
    
except:
    print("number cna't divide by zero")
    
else:
    print(f"Answer is : {c}")