# Write a Python program to convert a list of tuples into a dictionary.

school = [(1,'ayush',True), (2,'jiger',False), (3,'jay',False)]     #list of tuple
dict = {}

ran = 0
for i in range(1,len(school)+1):
    dict[i] = school[ran]   #list of tuple to dict
    ran += 1  
print(dict)