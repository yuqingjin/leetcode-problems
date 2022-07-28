# Method: DFS, backtracking
# Basic idea: DFS, start from each cell discovering its four direcitions
# Time Complexity: O(m*n*dfs); dfs = 4^len(word)
# Space Complexity: O(len(word)), stored in set

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # 做法1：
        m, n = len(board), len(board[0])
        visit = set()
        
        def dfs(row, col, i):
            
            # base case1: find the word
            if i == len(word):
                return True
            
            # base case2: not satisfy the requirement, return
            if not 0 <= row < m or not 0 <= col < n or board[row][col] != word[i] or (row,col) in visit:
                return False
            
            visit.add((row, col))
            
            # if one of the four direction has result True, then we gonna return True
            # only need one solution for this problem
            res = dfs(row+1, col, i+1) or \
                  dfs(row-1, col, i+1) or \
                  dfs(row, col-1, i+1) or \
                  dfs(row, col+1, i+1)
            
            # after dfs, remove the cell from visited
            visit.remove((row, col))
            
            return res
            
        # main func:
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
                
        return False
        

        
#         做法2：
#         m, n = len(board), len(board[0])
#         directions = [(-1,0), (1,0), (0,-1), (0,1)]

#         def dfs(i, x, y):
#             # 不满足情况的终止条件
#             if not 0<= i < len(word) or not 0<= x < m or not 0 <= y < n\
#             or board[x][y] != word[i]:
#                 return False
            
#             # 满足状况的终止条件
#             if i == len(word) - 1:
#                 return True
            
#             # 把当前正在遍历的字符变成警号，防止重复遍历
#             board[x][y] = "#"
#             # res.append(board[x][y])

#             for (dx, dy) in directions:
#                 new_x, new_y = x+dx, y+dy
#                 if dfs(i+1, new_x, new_y):
#                     return True
#             # 遍历完毕后，将他还原成原来的字符，方便后面遍历继续使用
#             board[x][y] = word[i]
        
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == word[0] and dfs(0, i, j):
#                     return True
#         return False

