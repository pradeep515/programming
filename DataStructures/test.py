
from collections import Counter

def jump(list):
    farthest = 0 
    for i in range(len(list)):
        if i > farthest:
            return False
        farthest = max (farthest, i + list[i])
    return True
    
if __name__ == "__main__":
    testlist = [1,2,0,0,7]
    print(jump(testlist))
