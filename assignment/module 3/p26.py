#Write a Python program to replace last value of tuples in a lis

list1=[(1,2,3,),(4,5,6,7),(8,9)]
new=int(input("enter you tuple new last value:"))
mlis=[]
print("befor replace:",list1)
for i in list1:
    mlis.append(i[:-1]+(new,))      #replace list in tuple last value
print("after replace:",mlis)    #display list
