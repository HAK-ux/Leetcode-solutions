class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # grid-based representation of a graph, input = 2d grid ; 1 represents land and 0 represents water
        # output = number of islands -> one or more 1s connected togerther (horizontally or vetically)
        # go through each position in the grid, once we find a 1, we can do dfs and change the connected 1s to 0s, keep traversing

        m, n = len(grid), len(grid[0])
        num_islands = 0

        def dfs(y, x):
            if x < 0 or y < 0 or y >= m or x >= n or grid[y][x] != "1":
                return
            
            grid[y][x] = "0"
            dfs(y, x+1)
            dfs(y, x-1)
            dfs(y+1, x)
            dfs(y-1, x) 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    num_islands += 1
        return num_islands