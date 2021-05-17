
def isPalindrome(str1):
    str2 = str1[::-1]
    if (str1 == str2):
        print('is palindrome')
    else:
        print("not palindrome") 


if __name__ == '__main__':
    str = "dad"
    isPalindrome(str)
