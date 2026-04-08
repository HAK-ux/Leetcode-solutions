class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        visit = set()

        queue.append((0, 0))
        visit.add((0, 0))
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        length = 0
        while queue:

            for i in range(len(queue)):

                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                for dr, dc in neighbors:
                    nr = r + dr
                    nc = c + dc

                    if min(nr, nc) < 0 or nr == ROWS or nc == COLS or (nr, nc) in visit or grid[nr][nc] == 1:
                        continue
                
                
                    queue.append((nr, nc))
                    visit.add((nr, nc))
            length += 1
        
        return -1

