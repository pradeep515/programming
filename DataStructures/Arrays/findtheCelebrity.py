def knows(a,b):
    return True

def findCelebrity( n: int) -> int:

    candidate = 0 
    for i in range(1,n):
        if knows(candidate, i):
            candidate = i

    for j in range(n):
        if j != candidate:
            if knows(candidate,j) or not knows(j,candidate):
                return -1
    return candidate

