
## IN THIS TWO SUM, THE LIST IS SORTED. 
def twosum_sorted(self, numbers: List[int], target: int) -> List[int]:
    resultlist = []
    left = 0
    right = len(numbers)-1
    while left<right:
        currentsum = numbers[left]+numbers[right]
        if currentsum == target:
            return [left+1, right+1]
        elif currentsum > target:
            right -= 1
        else:
            left += 1
    return []



if __name__ == "__main__":
    wordlist = [2,7,11,15]
    print(twosum_sorted(wordlist, 9))