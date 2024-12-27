from collections import defaultdict
def insertion(list,list2):

    for dates, lacts in zip(list, list2):
        print (dates, lacts)


                





        


if __name__ == "__main__":
    list = [1,4,5,-1,56,78,23]
    list2 = [4,5,7,9,56,78,23]
    print(insertion(list, list2))


