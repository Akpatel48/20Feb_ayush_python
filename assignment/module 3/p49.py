'''Write a Python function to check whether a number is in a given range'''

startr=int(input("enter starting range:"))
endr=int(input("enter end range:"))
find=int(input("enter you find number:"))
list1=[]
def rang():
    for i in range(startr,endr):
        list1.append(i)

    if find in list1:
        print(f"{find} is in the range")
    else:
        print(f"{find} is not in the range")
rang()