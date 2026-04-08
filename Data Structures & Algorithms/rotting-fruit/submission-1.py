class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc

                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 2 or not grid[nr][nc]:
                        continue
                    
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
                
            time += 1

        return time if fresh == 0 else -1

                    

                
