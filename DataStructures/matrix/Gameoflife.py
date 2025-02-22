def gameOfLife(self, board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    m, n = len(board), len(board[0])

    directions = [(-1,0),(0,-1),(0,1),(1,0),(-1,-1),(-1,1),(1,1),(1,-1)]


    def get_count_live_neighbours(i, j):
        count = 0
        for di, dj in directions:
            ni, nj = di + i, dj + j

            if 0 <= ni < m and 0 <= nj < n and (board[ni][nj] == 1 or board[ni][nj] == 2):
                count += 1
        return count

    for i in range(m):
        for j in range(n):
            live_neighbour_count = get_count_live_neighbours(i, j)

            if board[i][j] == 1:
                if live_neighbour_count < 2 or live_neighbour_count > 3:
                    board[i][j] = 2
            else:
                if live_neighbour_count == 3:
                    board[i][j] = 3

    for i in range(m):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] =0 
            elif board[i][j] == 3:
                board[i][j] = 1 
