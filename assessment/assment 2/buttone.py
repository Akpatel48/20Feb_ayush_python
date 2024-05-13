import tkinter
from tkinter import ttk
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
    m = tkinter.Tk()
    m.geometry('300x400')
    m.title('Manger item')
    def buttn(self):
        ttk.Button(self.m, text='insert', command=impor).place(x=150, y=100)
        ttk.Button(self.m, text='update',command=updat).place(x=150, y=150)
        ttk.Button(self.m, text='view',command=vie).place(x=150, y=200)
        self.m.mainloop()