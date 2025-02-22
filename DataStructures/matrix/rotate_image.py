
## logic is swap rows to columsn for i < j and then the second part is reverse the rows
def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):

            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix