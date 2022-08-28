# Method: simulation
# T： O((m+n)log((diagonal_length)))
# S：O(diagonal_length)

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        for j in range(n-1, -1, -1):
            start_j = j
            start_i = 0
            i = 0
            cur = []
            while 0 <= i < m and 0 <= j < n:
                cur.append(mat[i][j])
                i += 1
                j += 1
                
            cur.sort()
            while 0 <= start_i < m and 0 <= start_j < n:
                cur_num = cur.pop(0)
                mat[start_i][start_j] = cur_num
                start_i += 1
                start_j += 1
                
        for i in range(1, m):
            start_j = 0
            start_i = i
            j = 0
            cur = []
            while 0 <= i < m and 0 <= j < n:
                cur.append(mat[i][j])
                i += 1
                j += 1
                
            cur.sort()
            while 0 <= start_i < m and 0 <= start_j < n:
                cur_num = cur.pop(0)
                mat[start_i][start_j] = cur_num
                start_i += 1
                start_j += 1
                
        return mat
          
