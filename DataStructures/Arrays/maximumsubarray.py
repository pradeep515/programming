# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubArray = currentSubArray = nums[0]
        for num in nums[1:]:
            currentSubArray = max(num, currentSubArray +num ) # reset currentSubarray  to num if it values is -ve.
            maxSubArray = max(maxSubArray, currentSubArray)
        return maxSubArray
