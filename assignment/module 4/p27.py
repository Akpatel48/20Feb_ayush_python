#What is Instantiation in terms of OOP terminology?

'''- Instantiation in oop terminology is Creating an object of an class.
    - Class is just a blue print or design until we create an instance (object).
    - instance is used to call members, methods or constructor.'''

class stu:
    def __init__(self):
        self.name=input("enter name:")
        self.roll_no=int(input("enter roll number:"))
class stushow(stu):
    def show(self):
        print(f"name:{self.name}")
        print(f"roll no:{self.roll_no}")
st=stushow()
st.show()