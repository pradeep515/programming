#Rotate array in place by ksteps to the right side .
#Approach:
# Normalize k: Since rotating the array n times results in the same array, rotating it k times is equivalent to rotating it k % n times. This reduces unnecessary rotations if k is larger than the array size.

# Reverse parts of the array: To perform the rotation in place, we can reverse three parts of the array:

# Reverse the entire array.
# Reverse the first k elements.
# Reverse the remaining n-k elements.

def rotatearrayright(testlist, k):
    n = len(testlist)
    k = k % n
    testlist.reverse()
    testlist[:k] = reversed(testlist[:k])
    testlist[k:] = reversed(testlist[k:])
    return testlist

def rotatearrayleft(testlist, k):
    n = len(testlist)
    k = k % n 
    testlist[:k] = reversed(testlist[:k])
    testlist[k:] = reversed(testlist[k:])
    testlist.reverse()
    return testlist


if __name__ == "__main__":
    testlist = [1,2,3,4,5,6,7]
    testlistleft = [1,2,3,4,5,6,7]
    print(rotatearrayright(testlist,2))
    print(rotatearrayleft(testlistleft,2))