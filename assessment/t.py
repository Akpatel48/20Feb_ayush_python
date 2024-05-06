import tkinter
from tkinter import ttk,messagebox
tk=tkinter.Tk()
tk.title("Registration Form")
tk.geometry("300x400")
h=tkinter.Label(text="Please enter details below",background='yellow',width=100).pack()



class page2():
    def page():
        global name
        tkinter.Label(text='Name*').place(x=1,y=30)
        name=tkinter.Entry()
        name.place(x=60,y=30)
        tkinter.Label(text='Contact*').place(x=1,y=70)
        tkinter.Entry(validate='all').place(x=60,y=70)
        tkinter.Label(text='Email*').place(x=1,y=110)
        tkinter.Entry().place(x=60,y=110)
        tkinter.Label(text='Gender').place(x=1,y=150)
        tkinter.Radiobutton(text='Male',value=1).place(x=60,y=150)
        tkinter.Radiobutton(text='Female',value=0).place(x=120,y=150)
        tkinter.Label(text="City*").place(x=1,y=190)
        city=['Rajkot','Ahmedabad','Baroda','Surat','Jamnagar']
        ttk.Combobox(values=city).place(x=60,y=190)
        tkinter.Label(text='State*').place(x=1,y=230)
        ttk.Combobox(values=city).place(x=60,y=230)
    def mass():
        messagebox.showinfo("Welcome",f"Firstname:{name.get()}\n")
        messagebox.OK()
    ttk.Button(text='Register').place(x=90,y=280)
class home():
    def hom():
        tkinter.Label(text='manger').place(x=1,y=30)
        tkinter.Button(text='manger').place(x=60,y=30)
        
home.hom()

la=tkinter.Label(text='fill the empty field!!!').place(x=70,y=255)
tkinter.mainloop()
