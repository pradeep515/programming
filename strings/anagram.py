
from collections import Counter
#easy method
def anagram(str, str1):
    str = sorted(str)
    str1 = sorted(str1)
    if str == str1:
        print("is anagram")
    else:
        print("not an anagram")

# easy method 2 
def anagram1(str1, str2):
    dict1 = Counter(str1)
    dict2 = Counter(str2)
    print (dict1)
    print (dict2)
    return dict1 == dict2

if __name__ == '__main__':
    str = "listen"
    str1 = "silent"
    print(anagram1(str, str1))
