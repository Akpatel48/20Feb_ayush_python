#How can you pick a random item from a range? 

import random

start=int(input("enter start number"))  #get start number
end=int(input("enter end number"))  #get end number
ran=random.randint(start,end)   #gnret number 
print(ran)  #display number