'''Write python program that user to enter only odd numbers, else will 
raise an exception.'''

no=int(input("enter numbere:"))
try:

    if no%2==0:
        print('number is even')
except:
    print('Enter odd number')
