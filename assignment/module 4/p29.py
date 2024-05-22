'''What relationship is appropriate for Course and Faculty?'''
      
#- Course Faculty share the Multiple Inheritance. 
#- e.g.


class Course :
    
    course : str
    
    def __init__(self):
        self.course  = input("Enter Course Name : ")
Course()