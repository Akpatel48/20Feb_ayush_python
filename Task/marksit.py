sub1=int(input("Enter first subject marks"))
sub2=int(input("Enter second subject marks"))
sub3=int(input("Enter third subject marks"))
sub4=int(input("Enter fourth subject marks"))
totle=sub1+sub2+sub3+sub4
print("your totle marks",totle)
if totle>80:
    print("First class")
elif totle>1:
    print("second class")
elif totle>40:
    print("pass class")
else:
    print("File")
