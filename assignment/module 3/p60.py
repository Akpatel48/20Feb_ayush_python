#Write a Python program to calculate the area of a trapezoid

top = int(input("enter value of top:"))
base = int(input("enter value of base:"))
height = int(input("enter value height:"))

area = (top+base)/height * 3
print(f"area of trapezoid is:{area}")