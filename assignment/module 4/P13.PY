#Explain Exception handling? What is an Error in Python?

no=input("enter number:")
try:    #Exception 
    for i in range(1,11):
        print(f"{no}*{i}={int(no)*i}")
except Exception as e:
    print(e)    #display error

print("Run program successful !!")