def mergesort(array):
    if(len(array)> 1):
        mid = len(array)//2    
        left = array[:mid]
        right = array[mid:]
        mergesort(left)   
        mergesort(right)
        k=i=j=0
        while(i<len(left) and j< len(right)):     
            if(left[i]<right[j]):
                array[k] = left[i]
                i = i+1
            else:
                array[k] = right[j]
                j= j+1
            k = k +1
        while(i<len(left)):
            array[k] = left[i]
            i= i+ 1
            k= k +1
        while(j<len(right)):
            array[k]= right[j]
            j = j+1
            k = k +1
    return array

if __name__ == "__main__":
    listtobesorted = [6,77,44,66,77,88,66,444,55,665,333,332]
    print (listtobesorted)
    sortedlist = mergesort(listtobesorted)
    print (sortedlist)