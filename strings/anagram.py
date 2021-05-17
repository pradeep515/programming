

def anagram(str, str1):
    str = sorted(str)
    str1 = sorted(str1)
    if str == str1:
        print("is anagram")
    else:
        print("not an anagram")

if __name__ == '__main__':
    str = "test"
    str1 = "estt"
    anagram(str, str1)
