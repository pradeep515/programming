class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        columns = len(grid[0])
        islands = 0 

        if not grid:
            return 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= columns or grid[i][j] == '0':
                return
            grid[i][j] = '0'

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1
        return islands
