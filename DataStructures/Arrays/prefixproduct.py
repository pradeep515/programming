# product in an array except self


def prefixproduct(testlist):
    res = [1] * len(testlist)
    prefix = 1
    postfix = 1
    for i in range(len(testlist)): 
        print (i)
        res[i] = prefix
        prefix *= testlist[i] 
        print (res)
    for j in range(len(testlist) -1, -1, -1):
        # what ever prefix value is already there in testlist[j] shoould be multipled 
        # by postfix , hence the below statement
        res[j] *= postfix  
        postfix *= testlist[j]
    return res
         

if __name__ == "__main__":
    testlist = [2,4,3,5]
    print(prefixproduct(testlist))