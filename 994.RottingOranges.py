# Method: BFS
# T: O(m*n)
# S: O(m*n)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0),(-1,0)]
        time = -1
        q = []
        fresh = 0
        
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
                    
        # edge case 1: only contain empty cells
        if len(q) == 0 and fresh == 0:
            return 0
        
        # edge case 2: no rotten oranges, impossible to has zero fresh oranges
        elif len(q) == 0 and fresh != 0:
            return -1
        
        while q:
            length = len(q)

            for i in range(length):
                x, y = q.pop(0)
                for dx, dy in directions:
                    n_x, n_y = x+dx, y+dy
                    if 0 <= n_x < row and 0 <= n_y < col and grid[n_x][n_y] == 1:
                        fresh -= 1
                        grid[n_x][n_y] = 2
                        q.append((n_x, n_y))
            time += 1
            
            
        return time if not fresh else -1
