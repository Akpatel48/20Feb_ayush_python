ac_no:int
ac_holder_name:str
ac_type:str
balance:int

'''def account():
    global ac_no
    global ac_holder_name
    global ac_type
    ac_no=int(input("enter A/C number:"))
    ac_holder_name=input("enter A/C holder name:")
    '''
def a_type():
    global ac_type
    ac_type=input("enter A/C type saving or current\n")
    if ac_type=='saving':
        print("your account openig type saving")
    elif ac_type=='current':
        print("your account openig type current")

def deposite():
    global balance
    balance=int(input("enter deposite amount:"))
    if balance>=2000:
        print("amount add")
    else:
        print("sorry deposite amount not lass thne 2000")

def withdrwal():
    global balance
    wi_balance=int(input("enter withdrwal amount:"))
    if wi_balance<=balance:
        balance-=wi_balance
        if balance<=1999:
            print("you not windro")
            balance+=wi_balance
    else:
        print("enter valid amount")
    
def account_ditle():
    print("A/C type",ac_type)
    print("A/C blance",balance)
#account()
'''deposite()
withdrwal()
account_ditle()'''