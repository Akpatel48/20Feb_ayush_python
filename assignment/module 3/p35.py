#How Do You Traverse Through A Dictionary Object In Python? 

list1=['id','name','salary']    #create list
dis={}      #creat dictionary

for i in list1:
    data=input(f"enter {i}:")   #get data in dic
    dis[i]=data     

for i in dis.items():
    print(i)