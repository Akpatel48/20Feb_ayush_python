name=input("enter your name: ")
print(name.isalpha())
if name.isalpha():
    age=input("enter your age: ")
    print(age.isdigit())
    if age.isdigit():
        email=input("enter your email addres: ")
        print(email.islower())
        if email.islower():
            epass=input("enter your password: ")
            print(epass.isalnum())
            if epass.isalnum():
                cpass=input("confrom password: ")
                if cpass==epass:
                    print(cpass.isalnum())
                    if cpass.isalnum():
                        mobile=input("enter your mobile number: ")
                        mo=mobile.__len__()
                    if mo==10:
                        print(mobile.isdigit())
                    else:
                        print("enter valid number")
                else:
                    print("enter valid pasword")