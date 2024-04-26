'''Write a Python program to combine two dictionary adding values for 
common keys. 
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} 
Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).'''

d1={}
d2={}
d3={}
no=int(input("enter no of paire you enter:"))

for i in range(no):
    key=input("enter first dictionary key:")
    value=input("enter first dictionary values")
    d1[key]=value

for i in range(no):
    key=input("enter secand dictionary key:")
    value=input("enter secand dictionary values")
    d2[key]=value

for i in d1:
    for j in d2:
        if i==j:
            d3[i]=int(d1[i])+int(d2[j])
        else:
            d3[i]=d1[i]
            d3[j]=d2[j]
print(d3)
