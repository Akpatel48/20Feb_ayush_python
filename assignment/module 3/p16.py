'''Write a Python program to check whether a list contains a sub list '''
lis1=[1,2,3,4,5,6,7,8]
lis=[2,5,7]
res=0
for i in lis:
    if i in lis1:
        res+=1
if res==len(lis):
    print("T")
else:
    print("F")