                                        #Run this page
import tkinter as tk
from tkinter import ttk
import re_login

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x400')
        self.root.title("Login")
        self.create_widgets()

    def create_widgets(self):
        self.login_button = ttk.Button(self.root, text='Login', command=self.login)     #login buttone
        self.login_button.place(x=120, y=150)

        self.register_button = ttk.Button(self.root, text='Register', command=self.register)    #register bu
        self.register_button.place(x=120, y=180)

    def login(self):
        try:
            login_module = re_login.log()   #jump to re_login librarie
            login_module.login()        #jump to login re function librarie
        except Exception as e:
            print(f"Error during login: {e}")

    def register(self):
        try:
            registration_module = re_login.res()        #jump to re_login librarie
            registration_module.Re()    #jump to re_login re function librarie
        except Exception as e:
            print(f"Error during registration: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()