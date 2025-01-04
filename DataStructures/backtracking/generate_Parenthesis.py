def generate_parenthesis(n):
    result = []

    def backtrack_generate_parenthisis(currentstring, opencount, closecount):

        if len(currentstring) == 2*n:
            result.append(currentstring)

        if opencount < n:
            backtrack_generate_parenthisis(currentstring +'(' , opencount+1, closecount)

        if closecount < opencount:
            backtrack_generate_parenthisis(currentstring +')', opencount, closecount+1)

    backtrack_generate_parenthisis('',0,0)
    return result
 





        





if __name__ == '__main__':
    n = 3
    print(generate_parenthesis(n))