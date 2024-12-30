
# max circularsubarraysum  = max(linersum , cirularsum)
# to find ciruclar sum formual is  Cirucularsum = totalsum(array) - minsubarrayvalue
def maxSubCircularArray(nums):

    totalsum = sum(nums)

    def minsubarray(nums):

        minvalue, currrentvaluemin = nums[0], nums[0]
        
        for value in nums[1:]:
            currrentvaluemin = min(value, currrentvaluemin + value)
            minvalue = min(minvalue, currrentvaluemin)

        return minvalue
    

    def maxsubarray(nums):
        maxvalue, currentvalue = nums[0], nums[0]
        
        for value in nums[1:]:
            currentvalue = max(value, currentvalue + value)
            maxvalue = max(maxvalue, currentvalue)

        return maxvalue

    
    minvalue_normal = minsubarray(nums)
    maxvalue_normal = maxsubarray(nums)
    if totalsum == minvalue_normal:
        return maxvalue_normal
    max_circularsum = totalsum - minvalue_normal

    maxcircularvalue = max(max_circularsum, maxvalue_normal)
    return maxcircularvalue

    


    

if __name__ == "__main__":
    nums = [-3,-2,-3]
    print(maxSubCircularArray(nums))