'''Write a Python class named Rectangle constructed by a length and 
width and a method which will compute the area of a rectangle '''

class Rectangle:
    def get(self):
        try:
            global length,width
            length=int(input("enter rectangle length:"))
            width=int(input("enter rectangle width:"))
        except Exception as er:
            print(er)
    def area(self,l,w):
        print("area of rectangle:",l*w)
re=Rectangle()
re.get()
re.area(length,width)