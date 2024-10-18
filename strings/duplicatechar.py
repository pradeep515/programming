# if a string is given , supress consecutive duplicates 

def duplicateremover(name):
    if name == None:
        return
    else:
        nonduplicate = []
        for char in name:
            index = len(nonduplicate)
            # print(index)
            if index == 0 or char != nonduplicate[index-1]:
                nonduplicate.append(char)
                # print(nonduplicate)
        return ''.join(nonduplicate)


if __name__ == '__main__':
    name = 'aaabdcss'
    print(duplicateremover(name))

