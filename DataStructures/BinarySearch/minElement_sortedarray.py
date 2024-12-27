def minelement(nums):

    left , right = 0 , len(nums)-1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[right]:
            right = mid 
        else:
            left = mid + 1
    return nums[left]



if __name__=="__main__":
    nums = [4,5,6,7,0,1,2]
    print(minelement(nums))