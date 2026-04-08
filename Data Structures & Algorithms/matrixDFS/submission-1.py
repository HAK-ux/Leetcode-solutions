class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        

        def dfs(r, c):
            

            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1:
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            visit.add((r, c))

            count = 0
            for dr, dc in neighbors:
                count += dfs(r + dr, c + dc)
            
            visit.remove((r, c))
            
            return count
        
        
        return dfs(0, 0)
            
             