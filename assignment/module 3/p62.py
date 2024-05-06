'''Write a Python program to calculate surface volume and area of a 
cylinder'''

r = int(input("enter radius of cylinder:"))     #get radius
h = int(input("enter height of cylinder:"))     #get height
pi=3.14

svolume = (2*pi*r*h) + (2*pi*(r**2))    #calulet surface volume
    
print(f"surface volume of cylinder is : {svolume}\n-----------------------------")      #display surface vloueme
    
area = (pi*(r**2) * h)  #caluet cylinder area
    
print(f"area of cylinder is : {area}")  #display cylinder