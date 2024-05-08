'''Write a Python class named Circle constructed by a radius and two 
methods which will compute the area and the perimeter of a circle'''

class Circle:
    def get(self):
        try:
            radius=int(input("enter circle radius:"))
        except Exception as er:
            print(er)
        return radius
    def area(self,ra):
        print("area of circle:",3.14*ra*ra)
    def perimeter(self,ra):
        print("perimeter of circle:",3.14*3.14*ra)

ci=Circle()
a=ci.get()
ci.area(a)
ci.perimeter(a)