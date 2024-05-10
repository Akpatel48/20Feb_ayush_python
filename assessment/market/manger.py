import tkinter
from tkinter import ttk,messagebox
import pymysql
fm=tkinter.Tk()
fm.geometry('300x400')

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='market')
    cr=db.cursor()
    print("database conetted")
except Exception as er:
    print(er)
try:
    table='create table item (name varchar(20) primary key,qut integer(11),price integer(11))'
    cr.execute(table)
    print('table creatae')
except Exception as er:
     print(er)

class mange:
    def indert(self):
        tkinter.Label(text='name').place(x=30,y=50)
        self.name=tkinter.Entry()
        self.name.place(x=70,y=53)
        tkinter.Label(text='quit').place(x=30,y=80)
        self.quit=tkinter.Entry()
        self.quit.place(x=70,y=83)
        tkinter.Label(text='prise').place(x=30,y=110)
        self.price=tkinter.Entry()
        self.price.place(x=70,y=113)
        ttk.Button(text='inster',command=self.ins).place(x=30,y=140)
    def ins(self):
        name=self.name.get()
        quit=self.quit.get()
        price=self.price.get()
        try:
            cr.execute('insert into item values(%s,%s,%s)',(name,quit,price)) 
            db.commit()
        except Exception as er:
            print(er)
    def update(self):
        tkinter.Label(text='State*').place(x=10, y=230)
        select_query = "SELECT FROM register"
        cr.execute(select_query)

ma=mange()
ma.indert()
fm.mainloop()