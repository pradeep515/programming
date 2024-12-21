def searchinsertPosition(nums, target):

    left, right = 0, len(nums)-1 

    while left <= right:
        mid = left + (right - left) // 2  # Can you (left + right) //2 as well in python but in other languages , it causes integer overflow for larget numbers
        print (left, mid, right)
        if nums[mid] == target:
            return mid   
        elif target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]: 
            left = mid + 1
    return left


if __name__=="__main__":
    nums = [1,3,5,6]
    print(searchinsertPosition(nums, 2))
    