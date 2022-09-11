from heapq import *
class engineer:
    def __init__(self, s, e):
        self.s = s
        self.e = e

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        eff = []
        modulo = 10**9 + 7
        
        for s, e in zip(speed, efficiency):
            eff.append(engineer(s, e))
            
        eff.sort(key = lambda x:-x.e)
        
        q = []
        min_eff, sum_speed, perform = 0, 0, 0
        for e in eff:
            min_eff = e.e
            sum_speed += e.s
            heappush(q, e.s)
            perform = max(perform, min_eff * sum_speed)
            
            if len(q) == k:
                sum_speed -= heappop(q)
                
        return perform % modulo
