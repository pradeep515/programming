def isPalindrome(s: str) -> bool:
    s= s.lower().strip()
    print(s)
    p= ""
    for char in s:
        if char.isalnum():
            p += char
    print (p)
    if p == p[::-1]:
        return True
    return False

if __name__=='__main__':
    s = "A man, a plan, a canal: Panama"
    isPalindrome(s)