# Add two numbers without '+' operator
# convert the two numbers to add into binary(base 2) .
# then add the converted values (remember if the addition is 2 ie is 10 in base representation , put 0 and carry 1 )


def add(a,b):
    while(b != 0): 
        carry = a & b 
        a = a^b
        b = carry << 1 
    return a 

if __name__ =="__main__":
    print (add(100,15))
    
    
        