def permutate(nums):
    result = []
    if not nums:
        return [] 
    
    def backtrack(path, remaining):
        if not remaining:
            result.append(path)
            return
        
        for i in range(len(remaining)):
            candidate = remaining[i]
            backtrack(path+ [candidate], remaining[:i]+remaining[i+1:])

    backtrack([],nums)
    return result


if __name__ == "__main__":
    nums = ["a","b","c"]
    print(permutate(nums))