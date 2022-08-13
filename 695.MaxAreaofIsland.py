# Method: DFS
# Basic idea: return the num of cells(1) each time, when it is on the boundary, return 0
# T: O(M*N)
# S: O(M*N)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        
        def dfs(i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] != 1:
                return 0
            
            grid[i][j] = 2
            
            return (1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1))
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
                    
        return res
