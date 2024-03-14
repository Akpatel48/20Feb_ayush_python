#Write python program that swap two number with temp variable and without temp variable
a=int(input("enter first nuhmber:"))
b=int(input("enter second number:"))
'''tamp=a
a=b
b=tamp'''
(a,b)=(b,a)
print(f"b={b}")
print(f"a={a}")