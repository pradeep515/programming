from collections import Counter
def longest_substring(lstring):

    left, testset = 0 , set()
    max_substring_len = 0

    for right in range(len(lstring)):
        while lstring[right] in testset:
            testset.remove(lstring[left]) 
            left += 1
        testset.add(lstring[right])
        
        max_substring_len = max(max_substring_len, right-left+1)
    return max_substring_len

        


if __name__=="__main__":
    st = 'geekforgeeks'
    print(longest_substring(st))