import tkinter
from tkinter import ttk, messagebox
import logi

def login_action():
    logi.login()
def re():
    logi.Re()
tk = tkinter.Tk()
tk.geometry('300x400')

# Create buttons for login and registration
ttk.Button(text='Login', command=login_action).place(x=120, y=150)
ttk.Button(text='Register',command=re).place(x=120, y=180)

tk.mainloop()
