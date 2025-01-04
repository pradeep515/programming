# this is the combination sum where we can reuse the elements

def combinationsum(candidates, target):

    result = []

    def backtrack_combination(start, target, current_combination):

        if target == 0:
           result.append(list(current_combination))

        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue

            current_combination.append(candidates[i])
            backtrack_combination(i, target-candidates[i], current_combination)
            current_combination.pop()
        
    backtrack_combination(0, target, [])
    return result
        
    


    

if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7 
    print(combinationsum(candidates, target))