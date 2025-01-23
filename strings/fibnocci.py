# fibonacci numbers are the addition of the last two numbers in the stream

# time complexity if O(2/\n)
def fib(n):
    if(n <= 1 ):
        return n
    elif(n ==1 or n ==2):
        return 1
    else:
        return fib(n-1)+ fib(n-2)

#another way to do it using iterative time complexity is )(n)
def fib1(n):
    if n<0:
        raise ValueError("Input should be a positive integer")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        a,b = 0,1
        for i in range(2,n+1):
            a, b = b, a+b
            print(a,b)
        return b
    
if __name__ == '__main__':
    print(fib1(10))




