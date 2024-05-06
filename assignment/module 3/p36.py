#How Do You Check The Presence Of A Key In A Dictionary? 

no=int(input("enter number of paire enter:"))
dis={}  #creat dic

for i in range(1,no+1):
    data=input("enter dictionary values:")
    dis[i]=data

print(dis)
find=int(input("enter you find key:"))  #enter you find key

if find in dis.keys():
    print(f"dictionary {find}")
    print(dis[find])
else:
    print("you find key not exit in Dictionary")