#Can one block of except statements handle multiple exception?

try:
    a=.2
    b='3'

    a=+b 
    if a<b: 
        None
    print(a)    
except Exception as e:
    print(e)