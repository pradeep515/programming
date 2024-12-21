def search2dMatrix(matrix, target):

    noofrows, noofcolumns = len(matrix) , len(matrix[0])

    row , column = 0 , noofcolumns-1

    while row < noofrows and column >= 0:
       if target == matrix[row][column]:
           return True
       elif target > matrix[row][column]:
           row  += 1
       else:
           column -= 1

    return False

   
       
if __name__=="__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(search2dMatrix(matrix, 11))