'''Write a Python function to get the largest number, smallest num and sum 
of all from a list.'''
l=[]    #creat list
size=int(input("enter number of element: "))    #size of list element
for i in range(size):
    li=int(input("enter element values: "))     #enter list data
    l.append(li)    #add data

def states(num):
    ma=max(num)     #list max number
    sm=min(num)     #lsit min number
    su=sum(num)     #list sum all number
    return ma,sm,su
max,small,sum=states(l)
print(f"max number: {max}")        #display max number
print(f"sumall number :{small}")    #display small number
print(f"sum of number : {sum}"  )   #sum all number