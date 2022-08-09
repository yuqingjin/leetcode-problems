# Method: heap queue
# Time: O(NlogN)
# Space: O(N)

import heapq as h
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        cur = 0
        q = []
        courses = sorted(courses, key = lambda x:x[1])
        
        for c in courses:
            if cur + c[0] <= c[1]:
                h.heappush(q, -c[0])
                cur += c[0]
            elif cur + c[0] > c[1] and q and q[0] < -c[0]:
                cur += q[0]
                h.heappop(q)
                h.heappush(q, -c[0])
                cur += c[0]
                
        return len(q)
