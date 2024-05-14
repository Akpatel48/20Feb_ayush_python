import tkinter
from tkinter import ttk
import in_up_vie

class ManageButtons:
    def __init__(self):
        self.m = tkinter.Tk()
        self.m.geometry('300x400')
        self.m.title('Manage items')
        self.create_buttons()
    def insert_item(self):
        ma = in_up_vie.Manage()
        ma.insert()

    def update_item(self):
        ma = in_up_vie.Manage()
        ma.update()

    def view_items(self):
        ma = in_up_vie.Manage()
        ma.view()
        
    def create_buttons(self):
        ttk.Button(self.m, text='Insert', command=self.insert_item).place(x=120, y=100)
        ttk.Button(self.m, text='Update', command=self.update_item).place(x=120, y=150)
        ttk.Button(self.m, text='View', command=self.view_items).place(x=120, y=200)
        self.m.mainloop()

    
