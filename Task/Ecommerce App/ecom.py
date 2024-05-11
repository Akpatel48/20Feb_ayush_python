import pymysql

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='task')
    print("connect")
except Exception as er:
    print(er)
cr=db.cursor()
#create table
try:
    table='CREATE table item(id integer PRIMARY KEY,sname varchar(20),name varchar(20),price integer,qui integer)'
    cr.execute(table)
    print("table created")
except Exception as er:
    print(er)

class manger:
    def input(self):
        id=int(input("enter id:"))
        sname=input("enter saler name:")
        name=input("enter prodect name:")
        price=input("enter price:")
        quit=input("enter quit:")
        try:
            cr.execute('insert into item values(%s,%s,%s,%s,%s)', (id,sname,name,price,quit)) 
            db.commit()
        except Exception as er:
            price(er)
    def update(self):
        up=int(input("enter prodect id:"))
        try:
            upd=cr.execute('select id from item where id=%s',(up))
            if up==upd:
                uname=input("enter prodect name:")
                uprice=input('enter price:')
                uquit=input("enter quit")
                try:
                    cr.execute("update item ")
            else:
                print("not aveleble")
        except Exception as er:
            print(er)
        
ma=manger()
ma.update()