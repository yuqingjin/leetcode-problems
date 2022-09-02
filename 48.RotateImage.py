class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Method 2: continuously exchange four corner cells
        # T: O(N^2)
        # S: O(1)
        # (i,j) -> (j, (n-1)-i) -> ((n-1)-i, (n-1)-j) -> ((n-1)-j, i) -> (i, j) 
        n = len(matrix)
        for i in range(n//2 + n % 2):
            for j in range(n//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[(n-1)-j][i]
                matrix[(n-1)-j][i] = matrix[(n-1)-i][(n-1)-j]
                matrix[(n-1)-i][(n-1)-j] = matrix[j][(n-1)-i]
                matrix[j][(n-1)-i] = temp
        
        
#         Method 1: 
#         T: O(N^2)
#         S: O(N^2)
#         n = len(matrix)
#         copy = [[0] * n for _ in range(n)]
        
#         for i in range(n):
#             for j in range(n):
#                 copy[i][j] = matrix[i][j]
                
#         for i in range(n):
#             for j in range(n):
#                 # new position: [j][(n-1)-i]
#                 # old position: [i][j]
#                 if n-1-i > 0:
#                     matrix[j][n-1-i] = copy[i][j]
#                 else:
#                     matrix[j][i-(n-1)] = copy[i][j]
        
