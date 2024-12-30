
def getCombination(digits):
    result = [] 

    if not digits:
        return []
    
    telephonedict = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi'
    }

    def backtrack(index, combination):

        if index == len(digits):
            result.append(combination)
            return 
        
        current_digit = digits[index]
        for char in telephonedict[current_digit]:
            backtrack(index+1, combination+char)
        
    backtrack(0,"")
    return result


if __name__=="__main__":
    numsString = "234"
    print(getCombination(numsString))