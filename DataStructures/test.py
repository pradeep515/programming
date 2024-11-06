
from collections import Counter

def rotate(testlist,k):
    testlist = testlist[-k:]
    return testlist
    
if __name__ == "__main__":
    testlist = [1,2,3,4,5,6,7]
    print(rotate(testlist,3))
