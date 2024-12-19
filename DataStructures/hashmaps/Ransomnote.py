# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true    

def canConstruct(ransomNote, magazine):
        l1, l2 = 0, 0
        ransomNote = ''.join(sorted(ransomNote))
        magazine = ''.join(sorted(magazine))
        print(ransomNote)
        print(magazine)

        while l1 < len(ransomNote) and l2 < len(magazine):
            if ransomNote[l1] != magazine[l2]:
                return False
            l1 += 1 
            l2 += 1
        return True

if __name__=='__main__':
     str1 = "aab"
     str2 = "baa"
     print(canConstruct(str1, str2))