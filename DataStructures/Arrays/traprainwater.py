# Leetcode 42 problem - Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.
# 1st way 
def trap(self, height: List[int]) -> int:
    result = [0]*len(height)
    maxleft = 0
    maxright = 0
    compute = 0
    trappedwater = 0
    for i in range(0,len(height)):
        result[i] = maxleft
        if height[i] > maxleft:
            maxleft = height[i]
    for i in range(len(height)-1, -1, -1):
        compute = min(result[i], maxright)-height[i]
        if compute < 0 :
            result[i] = 0
        else:
            result[i] = compute
        if height[i] > maxright:
            maxright = height[i]
    for i in result:
        trappedwater += i
    return trappedwater

#2nd way :
def trap(self, height: List[int]) -> int:
    left,right = 0, len(height)-1
    maxleft, maxright,result = height[left], height[right],0
    while left<right:
        if maxleft < maxright:
            left +=1
            maxleft = max(maxleft, height[left])
            result += maxleft - height[left]
        else:
            right -=1
            maxright = max(maxright, height[right])
            result += maxright - height[right]
    return result
