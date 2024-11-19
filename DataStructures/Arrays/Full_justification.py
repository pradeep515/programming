
def fullJustify(words, maxWidth):
    current_length = 0
    current_line = []
    result = []
    for word in words:
        if current_length + len(current_line) + len(word) > maxWidth:
            result.append(justify(current_length,current_line,maxWidth))
            current_length = 0
            current_line = []
        current_line.append(word)
        current_length += len(word)
    last_line = " ".join(current_line)
    result.append(last_line + " " *( maxWidth - len(last_line)))
    return result
    

def justify(current_length, words, maxWidth):
    if len(words) == 1:
        return words[0]+ " " * (maxWidth - len(words[0]))

    total_spaces = maxWidth - current_length
    spaces_in_between = total_spaces//(len(words)-1)
    extra_spaces = total_spaces % (len(words)-1)

    line = words[0]
    for i in range(1, len(words)):
        if i <= extra_spaces:
            line += " " * (spaces_in_between +1)
        else:
            line += " " * (spaces_in_between)
        line += words[i]
    return line




if __name__ == "__main__":
    wordlist = ["This", "is", "an", "example", "of", "text", "justification."]
    print(fullJustify(wordlist,16))
