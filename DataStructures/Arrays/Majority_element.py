#return majaority element in an array .  We can do it using dictionary/hashmap in o(n) time and o(n) space
# but we need to do it in o(1) space complexity.
# We need to use Boyer-Moore Voting Algorithm for it

def majorityelement(testlist):
    count, candidate = 0, None
    for num in testlist:
        if count == 0:
            candidate = num
            count += 1
        elif candidate == num:
            count += 1
        else:
            count -= 1
    return candidate

 #time and space complexity for the above are O(n) and O(1) 


#  My other way in O(n) and O(n) is 
# from collections import Counter

# def majorityElement(testlist):
#     counterdict = Counter(testlist)
#     print (counterdict)
#     for key,value in counterdict.items():
#         if value > len(testlist)/2:
#             return key
       