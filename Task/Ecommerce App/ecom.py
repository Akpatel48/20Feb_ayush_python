import pymysql
try:
    db=pymysql.connect(host='localhost',user='root',password='',database='task')
    print("connect")
except Exception as er:
    print(er)
cr=db.cursor()
#create table
try:
    table='CREATE table item(id integer PRIMARY KEY AUTO_INCREMENT,sname varchar(20),name varchar(20),price integer,qui integer)'
    cr.execute(table)
    print("table created")
except Exception as er:
    print(er)

class manger:
    def input(self):
        try:
            sname = input("Enter seller name: ")
            name = input("Enter product name: ")
            price = int(input("Enter price: "))
            quantity = int(input("Enter quantity: "))

            try:
                cr.execute('INSERT INTO item(sname,name,price,qui) VALUES (%s, %s, %s, %s)', (sname, name, price, quantity))
                db.commit()
                print("Product inserted successfully!")
            except Exception as er:
                print("Error inserting product:", er)
        except ValueError:
            print("Invalid input. Please enter valid integer values for ID, price, and quantity.")
        except Exception as er:
            print("Error:", er)

    def update(self):
        try:
            up = int(input("Enter product id: "))
            cr.execute('SELECT id FROM item WHERE id=%s', (up,))
            upd = cr.fetchone()
        
            if upd:
                uname = input("Enter product name: ")
                uprice = input('Enter price: ')
                uquit = input("Enter quantity: ")
            
                try:
                    cr.execute('UPDATE item SET name=%s, price=%s, qui=%s WHERE id=%s', (uname, uprice, uquit, upd[0]))
                    db.commit()
                    print("Product updated successfully!")
                except Exception as er:
                    print("Error updating product:", er)
            else:
                print("Product ID not found!")  
        except Exception as er:
            print(er)

    def view(self):
        try:
            cr.execute('select * from item')
            vie=cr.fetchall()
            for i in vie:
                print(i)
        except Exception as er:
            print(er)

class customer():
    def purchase(self):
        try:
            name = input("Enter product name: ")
            cr.execute('SELECT id,qui FROM item WHERE name=%s', (name))
            buy = cr.fetchone()
            if buy:
                bquit =int(input("Enter quantity: "))
                if buy[1]>bquit:
                    temp=buy[1]
                    bquit=temp-bquit
                    try:
                        cr.execute('UPDATE item SET qui=%s WHERE id=%s', (bquit,buy[0]))
                        db.commit()
                        print("Product buy successfully!")
                    except Exception as er:
                        print("Error buy product:", er)
                else:
                    print("Product quit not inaf !")
            else:
                print("Product NAME not found!")
        except Exception as er:
            print(er)
ma=manger()
ca=customer()
def display():
    print("\t\t\tWelcome to Market")
    print('1.Product Manger\n2.Customer')
    try:
        role=int(input("Enter your role:"))
    except Exception as er:
        print(er)
    if role==1:
        print("1.INSER\n2.UPDATE\n3.VIEW")
        select=int(input("Enter you prform opresen:"))
        if select==1:
            ma.input()
        elif select==2:
            ma.update()
        elif select==3:
            ma.view()
    elif role==2:
        ca.purchase()
display()