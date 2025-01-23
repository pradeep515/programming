def depthSum(nestedList):
    
    
    def backtrack(elements, depth):
        max_val = 0
        for element in elements :
            if isinstance(element,list):
               max_val +=  backtrack(element, depth+1)
            else:
                max_val += element * depth
        return max_val
            
    max_val = backtrack(nestedList, 1)
    return max_val


if __name__=='__main__':
    nestedList = [[1,1],2,[1,1]]
    print(depthSum(nestedList))