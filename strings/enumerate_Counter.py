from collections import Counter

def countdict(charlist):
    #enumerate is used to get the index and value for the element.  Counter is used to get a dict object where
    #  element and its occurrences as counter are given
    for index , element in enumerate(charlist): 
        print (index , element)
    testdict = Counter(charlist)
    print (testdict)


    
if __name__ == "__main__":
    array = list("geekforgeeks")
    countdict(array)
   