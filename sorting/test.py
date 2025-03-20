from collections import Counter
def sort(nums):

   

    candidate_count = 0
    candidate = None
    i = 0 
    while i <= len(nums)-1:
        print(f'candidate {candidate}, count {candidate_count}')
        if candidate == nums[i] and candidate_count == 2:
            del nums[i]
            print(f'deleting this candidate {candidate}')
        elif candidate == nums[i] and candidate_count <2:
            candidate_count += 1
            i += 1
        elif candidate != nums[i]:
            candidate_count = 1
            candidate = nums[i]
            i += 1
    return nums 

       
if __name__=="__main__":

    nums = [1,1,1,2,2,3]
    print(sort(nums))