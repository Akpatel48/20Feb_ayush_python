import pymysql
import tkinter
from tkinter import ttk,messagebox

try:
    db = pymysql.connect(host='localhost', user='root', password='', database='market')
    cr = db.cursor()
    print("database connected")
except Exception as er:
    print(er)

    #customer
class customer:
    def __init__(self):
        self.fm = tkinter.Tk()
        self.fm.geometry('300x400')
    def buy(self):
        self.fm.title("CUSOTMER")
        try:
            select_query = "SELECT name FROM item"
            cr.execute(select_query)
            data=cr.fetchall()
        except Exception as er:
            print(er)
            messagebox.showerror("Error", "Failed to update")
        tkinter.Label(self.fm,text="Product").place(x=10, y=100)
        self.product = ttk.Combobox(self.fm,values=data)    #show product
        self.product.place(x=80, y=103)
        tkinter.Label(self.fm,text="qut").place(x=10, y=130)
        self.qut=tkinter.Entry(self.fm) #get bay quit
        self.qut.place(x=80,y=133)
        ttk.Button(self.fm,text='BAY',command=self.get).place(x=80,y=170)
        self.fm.mainloop()
    def get(self):  #get data in database
            nam=self.product.get()
            gquit=self.qut.get()
            try:
                cr.execute('SELECT qui FROM item WHERE name=%s',(nam))
                quit=cr.fetchone()
                if quit[0]>int(gquit):
                    temp=quit[0]
                    gquit=temp-int(gquit)
                else:
                    messagebox.showwarning("show prodect quit",f"this product qite max available:{quit}")
                    try:
                        cr.execute('UPDATE item SET qui=%s WHERE name=%s',(gquit,nam))
                        db.commit()
                    except Exception as er:
                        print(er)
            except Exception as er:
                print(er)