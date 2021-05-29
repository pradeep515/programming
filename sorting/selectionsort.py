#Selection sort
# Compare the fixed pointer with variable pointer(pointer next of fixed) and swap if fixed is greater than variable pointer, increment variable pointer
# increament fixed (variable pointer will be next of fixed)
#The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.

def selectionsort(array):
    for i in range(0,len(array)):
        for j in range(i+1, len(array)):
             if(array[i]>array[j]):
                 array[i],array[j] = array[j],array[i]

if __name__ == "__main__":
    array=[56,32,43,23,11,1]
    selectionsort(array)
    print(array)
