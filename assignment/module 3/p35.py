#How Do You Traverse Through A Dictionary Object In Python? 

list1=['id','name','salary']
dis={}

for i in list1:
    data=input(f"enter {i}:")
    dis[i]=data

for i in dis.items():
    print(i)