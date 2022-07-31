# Method: array
# Baic idea: record the minimum price, compute the profit each time and save the maximum one 
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
            
