#When will the else part of try-except-else be executed? 

try:
    a=int(input("enter number:"))
except Exception as b:
    print(b)
else:       #else part is anyway show
    print(a)
