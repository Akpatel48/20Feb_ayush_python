# Differentiate between append () and extend () methods?

list1=[1,2,3,4]
list2=[]
no=int(input("enter  number of element:"))
for i in range(no):
    li=int(input("enter element values:"))
    list2.append(li)
print(f"Before extend:\n\tlist1:{list1}\n\tlist2{list2}")
list1.extend(list2)
print('-------------------')
print("after extend",list1)