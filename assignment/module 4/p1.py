#What is File function in python? What is keyw to create and write file. 
'''
Q-1 : What is file function in pyhton?

- Python supports file handling and allows users to handle files i.e., to read and write files, along with 
   many other file handling options, to operate on files.   
- The key function for working with files in Python is the open() function.
- The open() function takes two parameters; filename, and mode.
- In Python, the open() function is used to create and open files.
- To create and write to a file, you typically use the mode 'w' (write mode) or 'a' (append mode) with the 
   open() function.
'''

# Open a file in create and write mode ('w')

f = open('my.txt','w')   #create or open file
f.write("This is Python")  #write in file
f.close()   #file close
f1 = open('my.txt', 'r')  
print(f1.read())    #read file