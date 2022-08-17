# Method: heap queue
# Time: O(N+NlogK)
# Space: O(n)
    
    
from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        
        for point in points:
            x, y = point
            cur = x**2 + y**2
            q.append([cur, x, y])
        
        heapify(q)
        res = []
        
        for i in range(k):
            minimum = heappop(q)
            res.append(minimum[1:3])
            
        # print(res)
        return res
