import math
# linear method
def squareroot(x):
    if (x == 0 or x ==1):
        return x
    else:
        for i in range(2,x):
            if (i*i >= x):
                return i-1

         

if __name__=="__main__":
    print(squareroot(50))

        