'''Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string. 
Sample string: 'w3resource' 
Expected output: 
{'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} '''

string=input('enter any word:')
dic={}
count = 1

for i in string:
    
    key = i
    if key not in dic:
        dic[key] = count
    else:
        dic[key] +=count
        
print(dic)