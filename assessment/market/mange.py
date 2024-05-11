import tkinter
from tkinter import ttk, messagebox
import pymysql

try:
    db = pymysql.connect(host='localhost', user='root', password='', database='market')
    cr = db.cursor()
    print("database connected")
except Exception as er:
    print(er)

try:
    table = 'create table item (name varchar(20) primary key, qut integer(11), price integer(11))'
    cr.execute(table)
    print('table created')
except Exception as er:
    print(er)

class Manage:
    def __init__(self):
        self.fm = tkinter.Tk()
        self.fm.geometry('300x400')
        
    def insert(self):
        self.fm.title("Insert prodect")
        tkinter.Label(self.fm, text='name').place(x=30, y=50)
        self.name = tkinter.Entry(self.fm)
        self.name.place(x=70, y=53)
        tkinter.Label(self.fm, text='quit').place(x=30, y=80)
        self.quit = tkinter.Entry(self.fm)
        self.quit.place(x=70, y=83)
        tkinter.Label(self.fm, text='price').place(x=30, y=110)
        self.price = tkinter.Entry(self.fm)
        self.price.place(x=70, y=113)
        ttk.Button(self.fm, text='insert', command=self.ins).place(x=70, y=140)
        self.fm.mainloop()
    def ins(self):
        name = self.name.get()
        quit_ = self.quit.get()
        price = self.price.get()
        try:
            cr.execute('insert into item values(%s,%s,%s)', (name, quit_, price)) 
            db.commit()
            messagebox.showinfo("Success", "Data inserted successfully")
        except Exception as er:
            print(er)
            messagebox.showerror("Error", "Failed to insert data")

    def update(self):
        self.fm.title("Update product dityle")
        try:
            select_query = "SELECT name FROM item"
            cr.execute(select_query)
            data=cr.fetchall()
            print(data)
        except Exception as er:
            print(er)
            messagebox.showerror("Error", "Failed to update")

        tkinter.Label(self.fm, text="Product").place(x=10, y=100)
        self.product = ttk.Combobox(self.fm, values=data)
        self.product.place(x=80, y=103)
        tkinter.Label(self.fm, text="qut").place(x=10, y=130)
        self.qut=tkinter.Entry(self.fm)
        self.qut.place(x=80,y=133)
        tkinter.Label(self.fm, text="price").place(x=10, y=160)
        self.pric=tkinter.Entry(self.fm)
        self.pric.place(x=80,y=163)
        ttk.Button(self.fm,text='UPDATE',command=self.upd).place(x=80,y=200)
        self.fm.mainloop()
    def upd(self):
        pr=self.product.get()
        q=self.qut.get()
        p=self.pric.get()
        try:
            cr.execute('update item set qut=%s,price=%s where name=%s',(q,p,pr))
            db.commit()
        except Exception as er:
            print(er)
            messagebox.showerror("Error", "Failed to insert data")
a=Manage()
a.update()