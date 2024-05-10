import sqlite3

try:
    db=sqlite3.connect('sql.db')
    print("connect")
except Exception as er:
    print(er)
table='create table admin(id integer PRIMARY KEY autoincrement)'
show='select * from admin'
try:
    db.execute(table)
    print('table created')
    db.commit()
except Exception as er:
    print(er)