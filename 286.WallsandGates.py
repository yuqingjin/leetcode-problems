# Method: BFS/DFS(tle)
# T: O(M*N)
# S: O(M*N), maximum queue size

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # method 2: BFS
        m, n = len(rooms), len(rooms[0])
        direct = [(0,1), (0,-1),(-1,0),(1,0)]
        
        q = []
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        
        steps = 1
        while q:
            leng = len(q)
            
            for i in range(leng):
                x, y = q.pop(0)
                for dx, dy in direct:
                    n_x, n_y = x+dx, y+dy
                    if 0 <= n_x < m and 0 <= n_y < n and (n_x, n_y) not in visited and rooms[n_x][n_y] >= steps:
                        rooms[n_x][n_y] = steps
                        q.append((n_x, n_y))
                        visited.add((n_x, n_y))
            steps += 1
                        
        
                        
                
            
            
        
#         def dfs(i, j, steps):
#             if not 0 <= i < m or not 0 <= j < n or rooms[i][j] < steps:
#                 return
            
#             if steps!= 0:
#                 rooms[i][j] = steps
            
#             for dx, dy in direct:
#                 dfs(i+dx, j+dy, steps+1)
            
#         for i in range(m):
#             for j in range(n):
#                 if rooms[i][j] == 0:
#                     dfs(i,j,0)
        
        
#         # method 1: DFS (TLE)
#         m, n = len(rooms), len(rooms[0])
#         direct = [(0,1), (0,-1),(-1,0),(1,0)]
        
        
#         def dfs(i, j, steps):
#             if not 0 <= i < m or not 0 <= j < n or rooms[i][j] < steps:
#                 return
            
#             if steps!= 0:
#                 rooms[i][j] = steps
            
#             for dx, dy in direct:
#                 dfs(i+dx, j+dy, steps+1)
            
#         for i in range(m):
#             for j in range(n):
#                 if rooms[i][j] == 0:
#                     dfs(i,j,0)
