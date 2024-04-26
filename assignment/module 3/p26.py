#Write a Python program to replace last value of tuples in a lis

list1=[(1,2,3,),(4,5,6,7),(8,9)]
new=input("enter you tuple nrw last value:")
mlis=[]
for i in list1:
    mlis.append(i[:-1]+(new,))
print(mlis)