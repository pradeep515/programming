# fibonacci numbers are the addition of the last two numbers in the stream


def fib(n):
    if(n <= 1 ):
        return n
    elif(n ==1 or n ==2):
        return 1
    else:
        return fib(n-1)+ fib(n-2)


if __name__ == '__main__':
    print(fib(9))

