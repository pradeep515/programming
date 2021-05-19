
#method1
def isPalindrome(str1):
    str2 = str1[::-1]
    if (str1 == str2):
        print('is palindrome')
    else:
        print("not palindrome") 

#method2 
def isPalindrome1(str1):
    for i in range(0, len(str1)/2):
        j = len(str1)-1
        if(str1[i]!=str1[j]):
            print("not palidrome")
            return
        else:
            j = j - 1
        print("palindrome")


if __name__ == '__main__':
    str = "lol"
    ispalindrome1(str)
