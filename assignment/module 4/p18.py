#When is the finally block executed?


try:
    a=int(input("enter any number:"))
except Exception as ab:
    print(ab)
finally:   
    print("program run successfully")