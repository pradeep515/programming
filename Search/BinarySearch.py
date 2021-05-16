array = [1,2,4,6,7,8,33,55,66]

# Search get the index of 7
def binarysearch(searchnumber, lower, upper):
    midpointer = lower+upper/2
    if(upper > lower):
        if(searchnumber == array[midpointer]):
            return midpointer
        elif(searchnumber<array[midpointer]):
            binarysearch(searchnumber, lower, midpointer-1)
        elif(searchnumber > array[midpointer]):
            binarysearch(searchnumber, midpointer+1, upper)
    else:
        return -1

