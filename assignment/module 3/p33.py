'''Write a Python script to concatenate following dictionaries to create a 
new one'''

no=int(input("enter number of paire enter:"))   #get number of pair in dict
dis1={} 
dis2={}

for i in range(1,no+1):
    data=input("enter first dictionaries values:")
    dis1[i]=data

for i in range(no+1,no+no+1):
    data=input("enter secand dictionaries values:")
    dis2[i]=data

dis1.update(dis2)

print(dis1)