def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findfirst():
            firstpos = -1
            left, right = 0 , len(nums)-1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    firstpos = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return firstpos 

        def findsecond():
            secondpos = -1
            left, right = 0 , len(nums)-1
            while left <= right:
                mid = left + (right - left) // 2 
                if nums[mid] == target:
                    secondpos = mid
                    left = mid + 1 
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return secondpos
        
        firstpos =  findfirst()
        secondpos = findsecond() if firstpos != -1 else -1
        return [firstpos, secondpos]