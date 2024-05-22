'''What relationship is appropriate for Student and Person?'''
   
#- For Student and person Multilevel inheritance is appropriate.
#- e.g.

class Person :
    
    def person(self,pr_name):
        
        self.pr_name = pr_name

class Student(Person):        
        
    def Student(self,s_name,s_course):
        
        print(f"\nStudent Name is : {s_name}")
        print(f"Student Course is : {s_course}")
        print(f"{self.pr_name} is Reference of {s_name}\n")
        
st = Student()

stName = input("Enter Student Name : ")  
stCourse = input("Enter Student Course : ")
prName = input("Enter Reference Person Name : ")

st.person(prName)
st.Student(stName,stCourse)