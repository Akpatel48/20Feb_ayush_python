import pywhatkit


#pywhatkit.sendwhatmsg_instantly("+919724799469","Hello Sanket, Good Afternoon!")
#pywhatkit.sendwhatmsg_to_group("20Feb_Python", "Hey All!",0,0)
#pywhatkit.sendwhatmsg_to_group_instantly("20Feb_Python", "Hey All!")

fl=open("number",'r')



for i in fl:
    print(i)
    pywhatkit.sendwhatmsg_instantly(i,"Hello Sanket, Good Afternoon!")