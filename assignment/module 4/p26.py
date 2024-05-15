#Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

'''- Constructor is a block of code the initialize newly created object.
      - Constructor is a method that is called automatically when we create the object of an class.
      - Generally constructor has the same name as the class name.
      - In Python Constructor is define with __init__ 
      - __init__ is a constructor in python and it doesn't have.'''

class a:
    def __init__(self):     #this method call automatically
        self.a=int(input("enter number:"))
        self.b=int(input("enter number:"))
class b(a):
    def __init__(self):
        super().__init__()
        print(self.a+self.b)
b()