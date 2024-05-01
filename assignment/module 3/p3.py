# Differentiate between append () and extend () methods?

list1=[1,2,3,4] #list 1
list2=[]    #list 2
no=int(input("enter  number of element:"))  #enter number element get
for i in range(no):
    li=int(input("enter element values:"))  #enter element data
    list2.append(li)                #add data in list
print(f"Before extend:\n\tlist1:{list1}\n\tlist2{list2}")
list1.extend(list2) #extend list1 and list2
print('-------------------')
print("after extend",list1)