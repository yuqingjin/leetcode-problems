# Method: DFS
# Basic idea: use reverse thinking; can be divided as three steps: 1.mark those unsurrounded regions, 2.flip surrounded regions, 3.unmark those unsurrounded regions
# T: O(n*m)
# S: O(n*m)
    
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def dfs(i, j, prev, mark):
            if i not in range(row) or j not in range(col) or board[i][j] != prev:
                return
            
            board[i][j] = mark
            for dx, dy in directions:
                n_x, n_y = i+dx, j+dy
                dfs(n_x, n_y, prev, mark)
        
        if row <= 2 and col <= 2:
            return 
        
        # step 1: mark unsurrounded regions 
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O" and (i in [0, row-1] or j in [0, col-1]):
                    dfs(i, j, "O","T")
                
        # step 2: flip surrounded regions 
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                    # 不知道为什么这样写不对
                    # dfs(i, j, "O", "X")

        # step 3: unmark unsurrounded regions 
        for i in range(row):
            for j in range(col):
                if board[i][j] == "T":
                    board[i][j] = "O"
                    # dfs(0, j, "T", "O")
