# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


def jump(jumplist):
    farthest = 0 
    for i in range(len(jumplist)):
        if i > farthest:
            return False
        farthest = max(farthest, i + jumplist[i])
        if farthest >= len(jumplist)-1: 
            return True
    return False
    
if __name__ == "__main__":
    testlist = [2,3,1,0,3]
    print(jump(testlist))