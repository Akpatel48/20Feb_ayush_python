'''What is used to check whether an object o is an instance of class A? '''
class A :
    
    def __init__(self) :
        print("This Is My Class")
        
o = A()
if(isinstance(o,A)):
    
    print("\no is an Instance of A")

else:
    print("o is not an Instance of A")