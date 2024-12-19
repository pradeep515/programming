def validParenthesis(s):

    bracketsdict = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    stack = []

    for char in s:
        if char in bracketsdict:
            stack.append(char)
        elif len(stack) == 0 or char != bracketsdict[stack.pop()]:
            return False
    return len(stack) == 0



if __name__ == "__main__":
    s = "{}}"
    print(validParenthesis(s))