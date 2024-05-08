#Write a python program to find the longest w.

f = open("txt.text",'r')   #open file in read mode

max_l = 0  #initialize variable
l_word = ""   #initialize variable

for line in f:
    w = line.strip().split()    #split the line
    for word in w:
        if len(word) > max_l:
            max_l = len(word)  #count length of word
            l_word = word 
        elif len(word) == max_l:   
            l_word += " " + word

print("Longest word : ",l_word)   #display longest word