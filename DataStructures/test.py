def insertionsort(nums):

    for i in range(1, len(nums)):
        j = i - 1
        key = list[i]
        while j >= 0  and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums
            



if __name__ == "__main__":

    list = [4,6,2,-1,9,55,33]
    print(insertionsort(list))






        

