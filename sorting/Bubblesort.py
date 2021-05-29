#Bubble sort

def Bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j]>array[j+1] :
                array[j],array[j+1] = array[j+1],array[j]


if __name__ == "__main__":
    array = [56,42,57,1,4,324,63,22]
    Bubblesort(array)
    print(array)