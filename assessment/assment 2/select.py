import tkinter
from tkinter import ttk
import in_up_vie

def impor():
    ma = in_up_vie.Manage()
    ma.insert()
def updat():
    ma=in_up_vie.Manage()
    ma.update()
def vie():
    ma=in_up_vie.Manage()
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