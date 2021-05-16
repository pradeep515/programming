#Reverse a string
# print(char)

def reverse1(str):
    if(len(str)<1):
        return str
    else:
        firstchar = str[0:1]
        remainingstring = str[1:]
        reversedstring = reverse1(remainingstring)+firstchar
    return reversedstring

def main():
    name = 'pradeep'
    str = reverse1(name)
    print(str)

if __name__ == "__main__":
    main()

