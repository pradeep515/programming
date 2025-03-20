from collections import defaultdict

teststack = [] 

def random(val):
    if val not in teststack:
        teststack.append(val)

def deletet(val):
    if val in teststack:
        del teststack[-1]
    
    


random(3)
random(4)
print(teststack)
deletet(3)
deletet(4)
print(teststack)













        

