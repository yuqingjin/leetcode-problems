# Method: 2-D pre-sum and binary select
# T: O(n^2*mlogm), 二分法将m降为logM；降之前，要确定start_row,end_row,start_col,end_col四个变量，所以是O((nm)^2)
# S: O(n)
# Follow up: if col and row has a large difference, we can choose the min(col, row) as the pre-sumed part. so the time complexity would be O(nm*min(m, n)*log(min(m,n)))

# 为了使用binaryselect, import sortedlist to maintain a sorted array
from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        cur_max = -inf
        
        # compute the horizontal pre-sum values
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]
        
        # set up start and end vertical value, 
        # and comput the pre-sum 
        for start in range(n):
            for end in range(start, n):
                pre = 0
                pres = SortedList([0])
                
                # 逐行计算
                for row in range(m):
                    pre += matrix[row][end] - (0 if start == 0 else matrix[row][start-1])
                    
                    # 二分法查找小于等于pre-k的最大值的index
                    index = pres.bisect_left(pre-k)
                    # 小于len(pres) 说明index存在
                    if index < len(pres):
                        cur_max = max(cur_max, pre - pres[index])
                    # sortedlist通过add添加新元素
                    pres.add(pre)
        return cur_max
