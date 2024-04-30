'''Write a Python program to calculate surface volume and area of a 
cylinder'''

r = int(input("enter radius of cylinder:"))
h = int(input("enter height of cylinder:"))
pi=3.14

svolume = (2*pi*r*h) + (2*pi*(r**2))
    
print(f"surface volume of cylinder is : {svolume}\n-----------------------------")
    
area = (pi*(r**2) * h)
    
print(f"area of cylinder is : {area}")