class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_sets = [set() for _ in range(9)]
        column_sets = [set() for _ in range(9)]
        grid_sets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue
                grid_index = (i // 3) * 3 + (j // 3)

                if num in row_sets[i] or num in column_sets[j] or num in grid_sets[grid_index]:
                    return False
                
                row_sets[i].add(num)
                column_sets[j].add(num)
                grid_sets[grid_index].add(num)
                
        return True
    



if __name__=="__main__":
    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    sudoku(board)