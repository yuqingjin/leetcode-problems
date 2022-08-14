# Method: backtracking
# T: O(N!)
# S: O(N^2)
     
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        res = []
        
        # 检查左上方和正上方，保证没有Queen
        # 还需要检查右上方
        def valid(x, y):
            if x == 0:
                return True
            
            # 正上
            for j in range(x-1, -1, -1):
                if board[j][y] == "Q":
                    return False
            
            # 左上
            i, k = x-1, y-1
            while i >=0 and k >= 0:
                if board[i][k] == "Q":
                    return False
                i -= 1
                k -= 1
                
            # 右上
            p, q = x-1, y+1
            while p >=0 and q < n:
                if board[p][q] == "Q":
                    return False
                p -= 1
                q += 1
                
            return True
        
        def backtracking(row):
            if row >= n:
                temp = []
                for i in range(n):
                    cur_row = "".join(board[i])
                    temp.append(cur_row)
                # print("temp", temp)
                res.append(temp)
                
            
            for col in range(n):
                if valid(row, col):
                    board[row][col] = "Q"
                    backtracking(row+1)
                    board[row][col] = "."
                    
            return
                    
        backtracking(0)
        return res
