import tkinter
from tkinter import ttk, messagebox
import mange

def impor():
    ma = mange.Manage()
    ma.insert()
def updat():
    ma=mange.Manage()
    ma.update()
def vie():
    ma=mange.Manage()
    ma.view()
class But:
    def buttn(self):
        m = tkinter.Tk()
        m.geometry('300x400')
        m.title('Manger item')
        ttk.Button(m, text='insert', command=impor).place(x=150, y=100)
        ttk.Button(m, text='update',command=updat).place(x=150, y=150)
        ttk.Button(m, text='view',command=vie).place(x=150, y=200)
        m.mainloop()


