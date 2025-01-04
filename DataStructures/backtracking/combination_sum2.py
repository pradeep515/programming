# IN this combinationsum, we should use only unique values. no duplicate values

def combinationsum(candidates, target):

    result = [] 

    def backtrack_combinationsum(start, target, current_combination):

        if target == 0:
            result.append(list(current_combination)) 
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break

            # if i > start and candidates[i] == candidates[i-1]:
            #     continue

            current_combination.append(candidates[i])
            backtrack_combinationsum(i, target-candidates[i], current_combination)
            current_combination.pop()
        
    candidates.sort()
    backtrack_combinationsum(0, target, [])
    return result
            





if __name__ == '__main__':
    candidates = [2,3,5]
    target = 8
    print(combinationsum(candidates, target))