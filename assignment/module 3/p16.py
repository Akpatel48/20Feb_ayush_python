'''Write a Python program to check whether a list contains a sub list '''
lis1=[1,2,3,4,5,6,7,8]  #create list
lis=[2,5,7] #create list
res=0
for i in lis:
    if i in lis1:
        res+=1
if res==len(lis):   #check sub list contains main list
    print("T")
else:
    print("F")