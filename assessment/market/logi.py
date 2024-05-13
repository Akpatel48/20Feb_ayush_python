import tkinter
from tkinter import ttk,messagebox
import pymysql
import buttone
try:
    db=pymysql.connect(host='localhost',user='root',password='',database='market')
    print('Database connected')
except Exception as er:
    print(er)
try:
    cr=db.cursor()
except Exception as er:
     print(er)
try:
    table='create table register (id varchar(20) primary key,name varchar(20),contact integer(11),email varchar(20),gender varchar(5),city varchar(20),state varchar(20),password varchar(16),role varchar(20))'
    cr.execute(table)
    print('table creatae')
except Exception as er:
     print(er)


class log:
    def login(self):
        tk = tkinter.Tk()
        tk.geometry('300x400')
        tk.title("login")
        tkinter.Label(tk, text='id').place(x=1, y=150)
        self.lid = tkinter.Entry(tk)
        self.lid.place(x=120, y=153)
        
        tkinter.Label(tk, text='password').place(x=1, y=180)
        self.pas = tkinter.Entry(tk)
        self.pas.place(x=120, y=183)
        
        ttk.Button(tk, text='Login', command=self.check).place(x=125, y=230)
        tk.mainloop()
        
    def check(self):
        try:
            entered_id = self.lid.get()
            entered_password = self.pas.get()
            
            # Retrieve data from the database
            try:
                select_query = "SELECT id, password FROM register WHERE id = %s AND password = %s"
                cr.execute(select_query, (entered_id, entered_password))
                row =cr.fetchone()
                if row==None:
                    messagebox.showerror(message="plice ente valid id or password")
            except:
                print("enter valid id password")

            if row:
                print("Login successful")
                select="select role from register where id=%s"
                cr.execute(select,(entered_id))
                role=cr.fetchone()
                print(role)
                a=buttone.But()
                a.buttn()
                if role=='Product Manager':
                    None
                else:
                    print("Incorrect ID or password")
        except Exception as er:
            print(er)
class res:

    def Re(self):
        tk=tkinter.Tk()
        tk.geometry('300x400')
        tk.title('Register Forme')
        tkinter.Label(tk,text='Please enter details below',background='yellow',width='100').pack()

        tkinter.Label(tk,text='id').place(x=10,y=50)
        self.id=tkinter.Entry(tk)
        self.id.place(x=80,y=53)

        tkinter.Label(tk,text='name').place(x=10,y=80)
        self.name=tkinter.Entry(tk)
        self.name.place(x=80,y=83)

        tkinter.Label(tk,text='Contect').place(x=10,y=112)
        self.con=tkinter.Entry(tk)
        self.con.place(x=80,y=113)

        tkinter.Label(tk,text='Email').place(x=10,y=140)
        self.email=tkinter.Entry(tk)
        self.email.place(x=80,y=143)

        tkinter.Label(tk, text='Gender').place(x=10, y=175)
        self.gender= tkinter.IntVar()
        tkinter.Radiobutton(tk, text='Male', value=0, variable=self.gender).place(x=80, y=175)
        tkinter.Radiobutton(tk,text='Female', value=1, variable=self.gender).place(x=150, y=175)

        tkinter.Label(tk, text="City*").place(x=10, y=200)
        city = ['Rajkot', 'Ahmedabad', 'Baroda', 'Surat', 'Jamnagar']
        self.city_combobox = ttk.Combobox(tk, values=city)
        self.city_combobox.place(x=80, y=203)

        tkinter.Label(tk, text='State*').place(x=10, y=230)
        state=['Gujarat','Goa','Chhattisgarh']
        self.state_combobox = ttk.Combobox(tk, values=state)
        self.state_combobox.place(x=80, y=233)

        tkinter.Label(tk,text='password').place(x=10,y=260)
        self.password=tkinter.Entry(tk)
        self.password.place(x=80,y=263)

        tkinter.Label(tk, text='Role').place(x=10, y=280)
        self.role= tkinter.IntVar()
        tkinter.Radiobutton(tk, text='Product Manager', value=0, variable=self.role).place(x=80, y=280)
        tkinter.Radiobutton(tk,text='Customer', value=1, variable=self.role).place(x=150, y=280)

        ttk.Button(tk,text='Register',command=self.register).place(x=55,y=320)
        ttk.Button(tk,text='home').place(x=150,y=320)
        tk.mainloop()
    def register(self):
        id=self.id.get()
        name =self.name.get()
        contact =self.con.get()
        email = self.email.get()
        gender = "Male" if self.gender.get() == 0 else "Female"
        city = self.city_combobox.get()
        state = self.state_combobox.get()
        password=self.password.get()
        role = "Product Manager" if self.role.get() == 0 else "Customer"
        print(id,name,contact,email,gender,city,state,password,role)
        '''try:
            cr.execute("INSERT INTO register VALUES (%s,%s,%s, %s, %s, %s, %s, %s,%s)", (id,name, contact, email, gender, city, state,password,role))
            db.commit()
        except Exception as er:
                print(er)'''
