import tkinter
from tkinter import ttk, messagebox
import pymysql


try:
    db = pymysql.connect(host='localhost', user='root', password='', database='market')
    print("Database connected")
    cr=db.cursor()
except Exception as er:
    print(er)

try:
    table = 'CREATE table item(id integer PRIMARY KEY AUTO_INCREMENT,sname varchar(20),name varchar(20),price integer,qui integer)'
    cr.execute(table)
    print("Table created")
except Exception as er:
    print(er)

class Manage:
    def __init__(self):
        self.fm = tkinter.Tk()
        self.fm.geometry('300x400')

    def insert(self):
        self.fm.title("Insert product")
        tkinter.Label(self.fm, text='Seller name').place(x=20, y=50)
        self.sname = tkinter.Entry(self.fm)
        self.sname.place(x=100, y=53)
        tkinter.Label(self.fm, text='Product name').place(x=20, y=80)
        self.name = tkinter.Entry(self.fm)
        self.name.place(x=100, y=83)
        tkinter.Label(self.fm, text='Quantity').place(x=20, y=110)
        self.quantity = tkinter.Entry(self.fm)
        self.quantity.place(x=100, y=113)
        tkinter.Label(self.fm, text='Price').place(x=20, y=140)
        self.price = tkinter.Entry(self.fm)
        self.price.place(x=100, y=143)
        ttk.Button(self.fm, text='Insert', command=self.insert_product).place(x=90, y=170)
        self.fm.mainloop()

    def insert_product(self):
        s_name = self.sname.get()
        name = self.name.get()
        quantity = self.quantity.get()
        price = self.price.get()
        if s_name and name and quantity and price:
            try:
                cr.execute('INSERT INTO item(sname,name,price,qui) VALUES (%s, %s, %s, %s)', (s_name, name, price, quantity))
                db.commit()
            except Exception as er:
                print("Error inserting product:", er)
                messagebox.showerror("Error", "Failed to insert data")

    def update(self):
        self.fm.title("Update product details")
        try:
            select_query = "SELECT name FROM item"
            cr.execute(select_query)
            data =cr.fetchall()
        except Exception as er:
            print(er)
            messagebox.showerror("Error", "Failed to update")
        tkinter.Label(self.fm, text="Product").place(x=10, y=100)
        self.product = ttk.Combobox(self.fm, values=[item[0] for item in data])
        self.product.place(x=80, y=103)
        tkinter.Label(self.fm, text="Quantity").place(x=10, y=130)
        self.qut = tkinter.Entry(self.fm)
        self.qut.place(x=80, y=133)
        tkinter.Label(self.fm, text="Price").place(x=10, y=160)
        self.pric = tkinter.Entry(self.fm)
        self.pric.place(x=80, y=163)
        ttk.Button(self.fm, text='UPDATE', command=self.update_product).place(x=80, y=200)
        self.fm.mainloop()

    def update_product(self):
        product = self.product.get()
        quit = self.qut.get()
        price = self.pric.get()
        try:
            cr.execute('update item set qui=%s,price=%s where name=%s', (quit, price, product))
            db.commit()
        except Exception as er:
            print(er)
            messagebox.showerror("Error", "Failed to update data")

    def view(self):
        try:
            select = 'SELECT * from item'
            cr.execute(select)
            data = cr.fetchall()
            print(data)
        except Exception as er:
            print(er)
        self.fm.geometry('400x500')
        self.fm.title('VIEW')
        for i, item in enumerate(data):
            tkinter.Label(self.fm, text=item).place(x=10, y=30 + i * 20)
        self.fm.mainloop()