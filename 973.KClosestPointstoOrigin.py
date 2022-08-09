# Method: heapq
# T: O(N+NlogK)
# S: O(N)

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        res = []
        
        for i, point in enumerate(points):
            x, y = point[0], point[1]
            leng = (x**2 + y**2)
            heap.append((leng, i))
                
        print(heap)
        
        for i in range(k):
            cur = heapq.heappop(heap)
            res.append(points[cur[1]])
        
        return res
