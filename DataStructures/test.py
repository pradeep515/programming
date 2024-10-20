
def palindrome(str):
    name = str
    frontpointer = 0
    backpointer = len(name)-1
    while frontpointer < backpointer:
        if name[frontpointer] == name[backpointer]:
            frontpointer = frontpointer+1
            backpointer = backpointer-1
        else:
            return False
    return True

if __name__ == "__main__":
    boolenavalue = palindrome("addadda")
    print(boolenavalue)
