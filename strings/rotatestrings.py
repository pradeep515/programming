#rotate string either left or right based on d numbers
def leftrotate(name, dspaces):
    rotatedstring = ''
    rotatedstring = name[dspaces:]+name[0:dspaces]
    print (rotatedstring)

def rightrotate(name, dspaces):
    rotatedstring = ''
    rotatedstring = name[-dspaces:]+name[:len(name)-dspaces] 
    print (rotatedstring)


def main():
    name = "Ramya"
    leftrotate(name, 3)
    rightrotate(name, 3)
    
if __name__ == '__main__':
    main()