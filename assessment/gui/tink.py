import tkinter
from tkinter import ttk, messagebox
import pymysql

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='test')
    print('Database connected')
except Exception as er:
    print(er)
cr=db.cursor()
try:
    table='create table login(name varchar(20),con integer(11),emil varchar(60),Gender varchar(20),city varchar(20),state varchar(20))'
    cr.execute(table)
    db.commit()
    print("table created")
except Exception as er:
    print(er)
class RegistrationForm:
    def page1(self,master):
        tkinter.Label(master, text="Please enter details below", background='yellow', width=100).pack()

        tkinter.Label(master, text='Name*').place(x=1, y=30)
        self.name_entry = tkinter.Entry(master)
        self.name_entry.place(x=60, y=30)

        tkinter.Label(master, text='Contact*').place(x=1, y=70)
        self.contact_entry = tkinter.Entry(master)
        self.contact_entry.place(x=60, y=70)

        tkinter.Label(master, text='Email*').place(x=1, y=110)
        self.email_entry = tkinter.Entry(master)
        self.email_entry.place(x=60, y=110)

        tkinter.Label(master, text='Gender').place(x=1, y=150)
        self.gender_var = tkinter.IntVar()
        tkinter.Radiobutton(master, text='Male', value=0, variable=self.gender_var).place(x=60, y=150)
        tkinter.Radiobutton(master, text='Female', value=1, variable=self.gender_var).place(x=120, y=150)

        tkinter.Label(master, text="City*").place(x=1, y=190)
        city = ['Rajkot', 'Ahmedabad', 'Baroda', 'Surat', 'Jamnagar']
        self.city_combobox = ttk.Combobox(master, values=city)
        self.city_combobox.place(x=60, y=190)

        tkinter.Label(master, text='State*').place(x=1, y=230)
        state=['Gujarat','Goa','Chhattisgarh']
        self.state_combobox = ttk.Combobox(master, values=state)
        self.state_combobox.place(x=60, y=230)

        ttk.Button(master, text='Register', command=self.register).place(x=90, y=280)

    def register(self):
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        email = self.email_entry.get()
        gender = "Male" if self.gender_var.get() == 0 else "Female"
        city = self.city_combobox.get()
        state = self.state_combobox.get()
        try:
            cr.execute("INSERT INTO login VALUES (%s, %s, %s, %s, %s, %s)", (name, contact, email, gender, city, state))
            db.commit()
            messagebox.showinfo("Welcome", f"Name: {name}\nContact: {contact}\nEmail: {email}\nGender: {gender}\nCity: {city}\nState: {state}")
        except Exception as er:
            print(er)

def main():
    root = tkinter.Tk()
    root.geometry('300x400')
    registration_form = RegistrationForm()  # Create an instance of RegistrationForm
    registration_form.page1(root)           # Call the page1 method on the instance
    root.mainloop()

if __name__ == "__main__":
    main()  