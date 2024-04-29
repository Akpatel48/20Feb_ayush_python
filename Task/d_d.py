data={}
stu=int(input("enter number of student"))
for i in range(stu):
    
    
    dict=input("enter dict name:")
    name=input("enter a name:")
    city=input("enter a  city")

    data[dict]={}

    data[dict]['name']=name
    data[dict]['city']=city

for i in range(stu):
    print(data)