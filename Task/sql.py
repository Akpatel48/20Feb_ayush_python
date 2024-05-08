import sqlite3

try:
    db = sqlite3.connect("tutorial.db")
    print("Connected to database successfully")
except Exception as e:
    print("Error:", e)


creat = '''CREATE TABLE stu (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(20),
                            city VARCHAR(20)
                        );'''


try:
    db.execute(creat)
    print("Table created successfully")
except Exception as e:
    print("Error:", e)

name=input("enter name:")
city=input("enter city:")

insert=f'insert into stu(name,city) values(?,?)'
try:
    db.execute(insert,(name,city))
    db.commit()
    print("Table created successfully")
except Exception as e:
    print("Error:", e)

