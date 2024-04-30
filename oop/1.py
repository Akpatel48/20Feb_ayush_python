#import os
#os.remove('1to100.txt')
main_bl=0
def diposit_bl():
     global main_bl
     main_bl=int(input("enter diposit balance: "))
wl_bl=0
def witheaw_bl():
    global wl_bl,main_bl
    wl_bl=int(input("enter withdow amount"))
    if main_bl>wl_bl:
        main_bl-=wl_bl
        try :
            if main_bl<2000:
                print("sorry you not witdorw your blance lesthen 2000")
        except:
            None
diposit_bl()
witheaw_bl()