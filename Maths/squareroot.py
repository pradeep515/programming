import math
# linear method
def squareroot(x):
    if x < 0:
        raise ValueError ("enter positive integers")
    i = 1 
    while i < x//2:
        if i * i > x :
            return i-1
        else:
            i += 1




         

if __name__=="__main__":
    print(squareroot(110))

        