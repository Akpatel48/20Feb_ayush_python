import tkinter
from tkinter import ttk, messagebox
import logi

def login_action():
    a=logi.log()
    a.login()
def re(): 
    a=logi.res()
    a.Re()
tk = tkinter.Tk()
tk.geometry('300x400')

# Create buttons for login and registration
lo=ttk.Button(text='Login', command=login_action).place(x=120, y=150)
ttk.Button(text='Register',command=re).place(x=120, y=180)
tk.mainloop()
