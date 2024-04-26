#How will you create a dictionary using tuples in python? 

tupl1=()
tupl2=()
no=int(input("enter no of element in tuple:"))
dic={}
for i in range(no):
    data1=input("enter key value:")
    data2=input("enter value:")
    tupl1+=(data1,)
    tupl2+=(data2,)

for i in range(no):
    dic[tupl1[i]]=tupl2[i]

print("\n",dic)