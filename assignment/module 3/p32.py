'''Write a Python script to sort (ascending and descending) a dictionary by 
value.'''

dict = {1 : 'mouse',2 : 'keyboard',3 : 'monitor',4 : 'cpu'}

ind = len(dict) #get dict len
print(f"Dictionary : {dict}\n")
print("Enter 'a' for ascending and 'd' for descending:")
choose = input("Enter Choice : ")   #get choice ascending or deseending oder

if (choose == 'a' or choose == 'A'):       #ascending oder
    
    print("Dictionary in ascending Order: ")
    for i in range(1, len(dict)+1):
        
        print(dict[i])
        
elif (choose == 'd' or choose == 'D'):
    
    print("Dictionary in descending Order:")
    for i in range(len(dict)):
        print(dict[ind])
        ind -= 1
        