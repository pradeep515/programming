# Quick sort 
#[12,14,15,13,89,23,44,131]
# 1) First mark the right most as the pivot index
# 2) move the values less the pivot index value to it left and greater values to its right (partitioner)
# 3) Then pass the left and right  side values of the pivot to the quick sort recursively .
# 

def quicksort(array, left , right):
    if(left <= right):
        pivot = array[(left+right)/2]
        partitionindex = partitioner(array, left, right, pivot)
        quicksort(array,left, partitionindex-1)
        quicksort(array, partitionindex, right)
    else:
        return

def partitioner(array , left , right, pivot):
    while(left <= right):
        while(array[left] < pivot):
            left++            #breaks when left element is greater than pivot so needs to be swapped
        while(array[right]> pivot):
            right--           #breaks when right element is less than pivot so needs to be swapped
        if(left<=right):
            array[left],array[right] = array[right],array[left]  #or swap(array,left, right)
            left++
            right--
    return left
        
                   