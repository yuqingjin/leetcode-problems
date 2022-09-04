# Method: simulation

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # method 2: simulation; T: O(N*M), S: O(1)
        m, n = len(board), len(board[0])
        
        def nextState(x, y):
            neigh = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if (x+dx) in range(m) and (y+dy) in range(n) and not (dx==0 and dy == 0) and abs(board[x+dx][y+dy]) == 1:
                        neigh += abs(board[x+dx][y+dy])
            
            # die: 1 to -1 (the absolute volue did not change)
            if board[x][y] == 1 and neigh not in range(2,4):
                return -1
            # reproduction: 0 to 2
            elif board[x][y] == 0 and neigh == 3:
                return 2
            # stay the original state
            else:
                return board[x][y]
        
        for i in range(m):
            for j in range(n):
                board[i][j] = nextState(i, j)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        
        # method1: simulation; T: O(N*M), S: O(N*M)
#         m, n = len(board), len(board[0])
#         new_board = [[board[i][j] for i in range(n)] for j in range(m)]
#         # for i in range(m):
#         #     for j in range(n):
#         #         new_board[i][j] = board[i][j]
        
#         def nextState(x, y):
#             neigh = 0
#             for dx in range(-1, 2):
#                 for dy in range(-1, 2):
#                     if (x+dx) in range(m) and (y+dy) in range(n) and not (dx==0 and dy == 0):
#                         neigh += new_board[x+dx][y+dy]
#             if neigh > 3 or neigh < 2:
#                 return 0
#             elif new_board[x][y] == 1 or (new_board[x][y] == 0 and neigh == 3):
#                 return 1
#             else:
#                 return 0
        
#         for i in range(m):
#             for j in range(n):
#                 board[i][j] = nextState(i, j)

