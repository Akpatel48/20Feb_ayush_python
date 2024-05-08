#How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets

import sqlite3

def get():
    try:
        name=input('enter name:')
        age=int(input("enter age:"))
        print(f"name:{name}\nage:{age}")
    except Exception as er:
        print(er)
        return 0 
    finally:
        print("program Run successfully")

get()