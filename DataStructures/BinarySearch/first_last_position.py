def searchRange(nums, target):
        result = [] 
        left, right = 0, len(nums)-1 
        
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                if nums[mid+1] == target:
                    result.append([mid, mid+1])
                elif nums[mid-1] == target:
                    result.append([mid-1, mid])
                return result[0]
            
            if target < nums[mid]:
                right = mid
            else:
                left = mid
            
        return result.append(-1,-1)

if __name__=="__main__":
    # nums = [5,7,7,8,8,10]
    nums = [] 
    print(searchRange(nums,0))