import tkinter
from tkinter import ttk,messagebox
tk=tkinter.Tk()
tk.title("Registration Form")
tk.geometry("300x400")
h=tkinter.Label(text="Please enter details below",background='yellow',width=100).pack()
class refm():
    def fro():
        
        tkinter.Label(text='Name*').place(x=1,y=30)
        tkinter.Entry().place(x=1,y=30)
        tkinter.Label(text='Contact*').place(x=1,y=70)
        tkinter.Entry().place(x=1,y=70)
        tkinter.Label(text='Email*').place(x=1,y=110)
        tkinter.Entry().place(x=1,y=110)
        tkinter.Label(text='Gender').place(x=1,y=150)
        tkinter.Radiobutton(text='Male',value=1).place(x=1,y=150)
        tkinter.Radiobutton(text='Female',value=0).place(x=120,y=150)
        tkinter.Label(text="City*").place(x=1,y=190)
        city=['Rajkot','Ahmedabad','Baroda','Surat','Jamnagar']
        ttk.Combobox(values=city).place(x=1,y=190)
        tkinter.Label(text='State*').place(x=1,y=230)
        ttk.Combobox(values=city).place(x=1,y=230)
        ttk.Button(text='Register').place(x=90,y=280)
refm.fro()
la=tkinter.Label(text='fill the empty field!!!').place(x=70,y=255)
tkinter.mainloop()
