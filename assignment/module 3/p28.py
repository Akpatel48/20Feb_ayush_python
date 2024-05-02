#Write a Python program to remove an empty tuple(s) from a list of tuples.
list1=[('python','java','c++'),('c','c#','koktile'),()]
print("before remove empty tuples:",list1)

for i in list1:
    if len(i)==0:   #remove empty  tuples
        list1.remove(i)

print("\nafter remove empty tuples:",list1)     #display list