
#Time Complexity: O(n^2) in the worst case.
# Space Complexity: O(n).
def findlongestsubstring(s):
     longestsubstring =""
     substring=''
     for i in s:
          if i not in substring:
               substring = substring + i
          else:
               if len(longestsubstring) < len(substring):
                    longestsubstring, substring = substring, i
     print (longestsubstring)
               

#another way to this with timecomplexity of o(n) is through sliding window
# Simple use a left and right pointer and increase the right pointer if the char is not a dup. if there is a dup, increment left pointer
#and pop the element in the set. maintain max len by comparing the current longest lenght and the window length.

def findlongestsubstring1(s):
     leftpointer,rightpointer,longestlength = 0,0,0 
     testset = set()
     for rightpointer in range(len(s)):
          while s[rightpointer] in testset:
               testset.remove(s[leftpointer])
               leftpointer += 1 
          testset.add(s[rightpointer])
          longestlength = max(longestlength, rightpointer-leftpointer+1)
     return longestlength

if __name__ == "__main__":
     name = 'geekforgeeks'
     print( findlongestsubstring1(name))