import random


with open('txt.text', 'r') as file:
        lines=file.readlines()
        num=len(lines)
        random=random.randint(0,num - 1)


print(f"Random line from the file : {lines[random]}")