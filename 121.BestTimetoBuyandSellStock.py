# Method: array
# Time: O(N)
# Space: O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minimum = prices[0]
        
        for i in range(1, len(prices)):
            res = max(res, prices[i]-minimum)
            minimum = min(minimum, prices[i])
        
        return res
            
