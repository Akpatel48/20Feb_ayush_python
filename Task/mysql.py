import pymysql

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='test')
    print('Database connected')
except Exception as er:
    print(er)
cr=db.cursor()
#create table
try:
    table='create table stu(id INTEGER PRIMARY KEY AUTO_INCREMENT,name varchar(20),city varchar(20))'
    cr.execute(table)
    db.commit()
    print("table created")
except Exception as er:
    print(er)
#insert data

'''try:
    insert=insert into stu(name,city) values('ayush','rajkot'),('jay','morbi'),('hepli','jamneger')
    cr.execute(insert)
    db.commit()
    print("recode inserted")
except Exception as er:
    print(er)'''
#show data
try:
    select='select * from stu'
    cr.execute(select)
    data=cr.fetchall()
    for i in data:
        print(i)
except Exception as er:
    print(er)