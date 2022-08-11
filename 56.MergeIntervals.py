# Method: sorting
# T: O(NlogN)
# S: O(N)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
#         第一遍
#         intervals = sorted(intervals, key = lambda x: (x[0], x[1])
        
#         for i in range(1, len(intervals)):
            
#             if res:
#                 prev = res[-1]
                
#                 if prev[1] < i[0]:
#                     res.append(i)
                    
#                 elif prev[0] <= i[0] and prev[1] >= i[1]:
#                     continue
                
#                 elif prev[0] <= i[0] <= prev[1] and prev[1] < i[1]:
#                     res[-1][1] = i[1]
            
#             else:
#                 res.append(i)
#         return res
        
    
        # 第二遍，优化简洁了一些
        intervals = sorted(intervals, key = lambda x: (x[0], x[1]))
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                cur = res.pop()
                left = min(cur[0], intervals[i][0])
                right = max(cur[1], intervals[i][1])
                res.append([left, right])
            else:
                res.append(intervals[i])
        return res
