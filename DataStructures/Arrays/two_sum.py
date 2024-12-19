## if given a list of unsorted value, find out indices which sum to a target
def twosum(list,target):
    valuedict = {}
    for index, num in enumerate(list):
        complement = target - num 
        if complement in valuedict:
            return (index, valuedict[complement])
        #if not in dict, add the num and it index
        valuedict[num] = index
    return []

# SECOND WAY 
def twosum_unsorted(list,target):
    indexednumbers = []
    for index, number in enumerate(list):
        indexednumbers.append((number,index))
    print(indexednumbers)
    indexednumbers.sort()
    print(indexednumbers)
    left = 0
    right = len(indexednumbers)-1
    while left < right:
        currentsum =  indexednumbers[left][0]+ indexednumbers[right][0]
        if currentsum == target:
            return [indexednumbers[left][1]+1, indexednumbers[right][1]+1]
        elif currentsum < target:
            left +=1 
        else:
            right -=1 
    return []




if __name__ == "__main__":
    list = [2,7,11,15]
    print(twosum(list, 9))