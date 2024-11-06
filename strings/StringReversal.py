#Reverse a string
# print(char)

def reverse(str):
    # Just reverses the string 
    return str[::-1]

def WordsReversed(sentence):
    #Reverse words in a string and removed any white spaces . ex ( I am blue -> blue am i )
    words = sentence.strip().split()
    words.reverse()
    return " ".join(words)

def findindex (name,name1):
    if name1 in name:
        index = name.find(name1)
        return index



if __name__ == "__main__":
    # reverse()
    # print(WordsReversed("I am blue"))
    print(findindex("pradeep","deep"))

