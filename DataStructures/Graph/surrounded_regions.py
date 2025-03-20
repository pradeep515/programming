def solve(board):
    if not board or not board[0]:
        return
    
    rows, cols = len(board), len(board[0])
    
    # DFS to mark 'O's connected to border
    def dfs(i, j):
        if (i < 0 or i >= rows or 
            j < 0 or j >= cols or 
            board[i][j] != 'O'):
            return
        board[i][j] = '#'  # Mark as safe
        # Explore all 4 directions
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    # Step 1: Mark 'O's on borders and their connected regions
    # Check first and last row
    for j in range(cols):
        if board[0][j] == 'O':
            dfs(0, j)
        if board[rows-1][j] == 'O':
            dfs(rows-1, j)
    
    # Check first and last column
    for i in range(rows):
        if board[i][0] == 'O':
            dfs(i, 0)
        if board[i][cols-1] == 'O':
            dfs(i, cols-1)
    
    # Step 2: Flip surrounded 'O's to 'X', restore '#' to 'O'
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '#':
                board[i][j] = 'O'

# Example usage
board = [['X', 'X', 'X', 'X'],
         ['X', 'O', 'O', 'X'],
         ['X', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'X']]
solve(board)
for row in board:
    print(row)