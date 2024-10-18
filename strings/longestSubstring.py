#longest substring with nonrepeating characters

longestsubstringcalculated = ''

def longestsubstring(name):
    global longestsubstringcalculated 
    substring = ''
    if(len(name)<=1):
        return
    for char in name:
        if(char not in substring):
            substring = substring + char
        else:
            # if(len(longestsubstringcalculated) < len(substring)):
            #     longestsubstringcalculated = substring
            # substring = ''
            if (len(longestsubstringcalculated) < len(substring)):
                   longestsubstringcalculated = substring
                   substring = char 
            else:
                   substring = char

        
if __name__ == '__main__':
    str = "GEEKSFORGEEKS"
    longestsubstring(str)
    print(longestsubstringcalculated)
   
    


