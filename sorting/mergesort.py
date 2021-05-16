array = [1,5,3,232,545,743,34,3]
def mergesort(array):
    if(len(array)> 1):
        mid = len(array)/2    
        left = array[:mid]
        right = array[mid:]
        mergesort(left)   
        mergesort(right)
        i=j=k=0
        newarray = []
        while(i<len(left) and j< len(right)):     
            if(left[i]<right[j]):
                newarray[k] = left[i]
                i = i+1
            else:
                newarray[k] = right[j]
                j= j+1
            k= k+1
        while(i<len(left)):
            newarray[k] = left[i]
            i= i+ 1
            k = k+1
        while(j<len(right)):
            newarray[k]= right[j]
            j = j+1
    else:
        return array