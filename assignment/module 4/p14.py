'''How many except statements can a try-except block have? Name Some built-in exception classes:

- An Exception is an Unexpected Event, which occurs during the execution of the program.   
- It is also known as a run time error.
- Exception handling with try, except, else, and finally block : 
    1.  Try :  This block will test the excepted error to occur
    2.  Except  :  Here you can handle the error
    3.  Else   :   If there is no exception then this block will be executed
    4.  Finally   :    Finally block always gets executed either exception is generated or not
'''

a=input("enter first number:")
b=input("enter secend number:")
try: 
	result = int(a)+int(b) 
except Exception as e: 
	print(e)
else:
	print("Yeah ! Your answer is :", result) 
finally: 
		# this block is always executed 
	print('This is always executed') 
