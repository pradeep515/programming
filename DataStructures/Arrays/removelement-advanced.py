# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element 
# appears at most twice. The relative order of the elements should be kept the same.

# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        testdict = {}
        i = 0
        while i < len(nums):
            if nums[i] in testdict:
                testdict[nums[i]] += 1
                if testdict[nums[i]] > 2:
                    del nums[i]
                    continue        
            else:
                testdict[nums[i]] = 1
            i = i + 1

        return len(nums)
    
# other way to do this is the following --- ONly change is incrementing when the condition is 2
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        testdict = {}
        i = 0
        while i < len(nums):
            if nums[i] in testdict:
                testdict[nums[i]] += 1
                if testdict[nums[i]] > 2:
                    del nums[i]
                    continue
                else:
                    i += 1
            else:
                testdict[nums[i]] = 1
                i = i + 1

        return len(nums)