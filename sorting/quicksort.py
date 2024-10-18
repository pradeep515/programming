""" 
1 - choose a pivot of your chooosing
2 - compare to pivot value and insert lesser values to left and higher values to right
3 - recursively call the function passing left and right and combine them and pivot as well .
"""


def quicksort(list_to_sort):
    if len(list_to_sort)<1:
        return list_to_sort
    pivot = list_to_sort[0]   # choosing the first element as the pivot
    left = []
    right = []
    for i in list_to_sort[1:]:    # leaving the pivot slot  and sorting go through the remaining elements
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    return quicksort(left)+[pivot]+quicksort(right) 

if __name__ == "__main__":
    list_to_sort = [1,2,3,4,45,22,66,323]
    sortedlist = quicksort(list_to_sort)
    print(sortedlist)
                   