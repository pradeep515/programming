def minWindow(s: str, t: str) -> str:
    
    left, right, index2 , current_word, min_word = 0, 0, 0,"", float("inf")

    while right < len(s) : 
        
        if s[right] in t:
            current_word = current_word + s[right]
            right += 1
            index2 += 1 
        else:
            current_word = current_word + s[right]
            right += 1 
            
            
        if index2 == len(t):
            while left < right:
                left += 1
        
    if min_word:
        return min_word
    else:
        return ""
        
if __name__ == "__main__":
    s,t ="ADOBECODEBANC","ABC"
    print(minWindow(s,t))
