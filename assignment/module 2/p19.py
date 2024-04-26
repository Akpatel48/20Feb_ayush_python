'''Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.'''
string=input("enter string:")   #get string
s1=string.find('not')
s2=string.find('poor')
if s1<s2:
    string=string.replace(string[s1:s2+4],'good')   #repace string
else:
    string=string.replace(string[s2:s1+3],'good')   #repace string
print(string)