'''Write a Python script to print a dictionary where the keys are numbers 
between 1 and 15. '''

no=int(input("enter no of dictionary pair:"))   #get number of pair in dic
key=int(input("enter you start key value:"))    #get key star value
dic={}

for i in range(key,no+key):
    data=input("enter dictionary value:")   #get dic values
    dic[i]=data

print(dic)  #display dic