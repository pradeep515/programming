#rotate string either left or right based on d numbers
def leftrotate(name, d):
    rotatedstring = ''
    rotatedstring = name[d:]+name[:d]
    print (rotatedstring)

def rightrotate(name, d):
    rotatedstring = ''
    rotatedstring = name[-d:]+name[:-d] 
    print (rotatedstring)


def main():
    name = "pradeep"
    leftrotate(name, 3)
    rightrotate(name, 3)
    
if __name__ == '__main__':
    main()