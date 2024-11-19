
def insertion(list):
    for i in range(1, len(list)):
        j = i - 1
        key = list[i]
        while j>=0 and key < list[j]:
            list [j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list    
             

if __name__ == "__main__":
    testlist = [1,2,0,0,7,4,3,22]
    print(testlist)
    print(insertion(testlist))
