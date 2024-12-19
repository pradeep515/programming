
def hindex(citations):
    citations.sort(reverse=True)
    for index, citation in enumerate(citations):
        print (index, citation)




if __name__ == "__main__":
    citations = [3,0,6,1,5]
    print(hindex(citations))
