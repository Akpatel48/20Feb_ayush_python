#Write python program that swap two number with temp variable and without temp variable
a=int(input("enter first nuhmber:"))
b=int(input("enter second number:"))    #input tow number
'''tamp=a   
a=b
b=tamp'''   #swap two number using threed variable 
(a,b)=(b,a) #swap two number with out threed variable
print(f"a={a} b={b}")
