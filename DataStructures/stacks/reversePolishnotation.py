def reversepolishnotation(tokens):
    if len(tokens) <=1:
        return tokens[0]
    
    result_stack = []
    operators = {
        '+': lambda a,b: a + b,
        '-': lambda a,b: a - b,
        '/': lambda a,b: int(a / b),
        '*': lambda a,b: a * b 
    }
    storage_stack = []

    for token in tokens:
        if token in operators:
            b = result_stack.pop()
            a = result_stack.pop()
            result = operators[token](a , b)
            result_stack.append(result)
        else:
            result_stack.append(int(token))

    return result_stack[0]
            

if __name__=="__main__":
    tokens = ["4","13","5","/","+"]
    # tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(reversepolishnotation(tokens))