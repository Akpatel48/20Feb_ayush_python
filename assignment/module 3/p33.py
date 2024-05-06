'''Write a Python script to concatenate following dictionaries to create a 
new one'''

no=int(input("enter number of paire enter:"))   #get number of pair in dict
dis1={}     #create dictionari
dis2={}     #create dictionari

for i in range(1,no+1):
    data=input("enter first dictionaries values:")  #get first dic values
    dis1[i]=data

for i in range(no+1,no+no+1):
    data=input("enter secand dictionaries values:") #get secand dic values
    dis2[i]=data    

dis1.update(dis2)   #concatenate dic1 and dic2

print(dis1)     #after conacatente 