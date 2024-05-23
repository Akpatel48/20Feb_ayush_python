#How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets

def get():
    try:
        name=input('enter name:')
        age=int(input("enter age:"))
        print(f"\nname:{name}\nage:{age}")
    except Exception as er:
        print(er)
    finally:
        print("\nprogram Run successfully")

get()