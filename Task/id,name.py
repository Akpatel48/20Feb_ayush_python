def data(id,name):
    return id,name

def ans():
    id=int(input("enter your id:"))
    na=input("enter your name:")
    a=data(id,na)
    print(a[0])
ans()