# Method: DFS
# T: O(M×N)
# S: O(M×N)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,-1), (0,1)]
        res = 0
        
        # 不需要return具体value， dfs的作用在本题只是为了标记岛屿，
        # 防止重复计数
        def dfs(x, y):
            
            # 这里必须三个条件都满足，才能继续
            if (not 0 <= x < m or not 0 <= y < n or grid[x][y] != '1'):
                return 
            
            grid[x][y] = '#'
            
            for (dx, dy) in directions:
                new_x, new_y = x + dx, y + dy
                dfs(new_x, new_y)
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res
