'''What relationship is appropriate for Student and Person?'''
   
#- For Student and person Multilevel inheritance is appropriate.
#- e.g.

class Person :
    
    def person(self):
        self.prname = input("Enter Reference Person Name : ")
       
class Student(Person):        
        
    def Student(self):
        sname = input("Enter Student Name : ")  
        scourse = input("Enter Student Course : ")
        print(f"\nStudent Name is : {sname}")
        print(f"Student Course is : {scourse}")
        print(f"{self.prname} is Reference of {sname}\n")
        
st = Student()
st.person()
st.Student()