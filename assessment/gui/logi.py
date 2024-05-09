import tkinter
from tkinter import ttk,messagebox



def login():
    tk=tkinter.Tk()
    tk.geometry('300x400')
    tkinter.Label(tk,text='Login').place(x=60,y=150)
    tkinter.Entry(tk).place(x=120,y=153)
    tkinter.Label(tk,text='password').place(x=60,y=180)
    tkinter.Entry(tk).place(x=120,y=183)
    ttk.Button(tk,text='Login').place(x=125,y=230)
    tk.mainloop()
def Re():
    tk=tkinter.Tk()
    tk.geometry('300x400')
    tkinter.Label(tk,text='Login').place(x=60,y=150)
    tkinter.Entry(tk).place(x=120,y=153)
    tkinter.Label(tk,text='password').place(x=60,y=180)
    tkinter.Entry(tk).place(x=120,y=183)
    ttk.Button(tk,text='Login').place(x=125,y=230)
    tk.mainloop()