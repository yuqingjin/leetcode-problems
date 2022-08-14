# Method: dfs
# Basic idea: from the border of matrix, traverse all the cells to find all the cells could flow to the specific ocean. find the intersection of cells of the two oceans set
# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m, n = len(heights), len(heights[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        P = set()
        A = set()
        
        def dfs(i, j, visited):

            if (i,j) in visited:
                return 
            visited.add((i,j))

            for dx, dy in directions:
                x, y = i+dx, j+dy
                if 0<= x < m and 0<= y < n and heights[x][y] >= heights[i][j]:
                    dfs(x, y, visited)

        
        # pacific start from [0, i] and [i, 0]
        # atlantic start from [m-1, 0] and [0, n-1]
        for i in range(m):
            dfs(i, 0, P)
            dfs(i, n-1, A)
            
        for j in range(n):
            dfs(0, j, P)
            dfs(m-1, j, A)
            
        return list(P & A)
