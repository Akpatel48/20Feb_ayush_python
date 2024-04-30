#How can you pick a random item from a range? 

import random

start=int(input("enter start number"))
end=int(input("enter end number"))
ran=random.randint(start,end)
print(ran)