from phonenumbers import carrier
import phonenumbers
p=input("enter number firt three + and contri code")
phone_number = phonenumbers.parse(p)
a=carrier.name_for_number(phone_number, 'en') 
print(a)
