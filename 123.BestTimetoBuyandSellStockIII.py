# Method: dp
# Basic idea of dp table: for each day, we have 5 states to choose
# no transaction, first time buy, first time sell, second time buy, second time sell
# Time: O(N)
# Space: O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # five choices of each day: no transaction, first time buy,
        # first time sell, second time buy, second time sell
        dp = [[0]*5 for i in range(len(prices))]
        
        # initiate dp table
        dp[0] = [0, -prices[0], 0, -prices[0], 0]
        
        for i in range(1, len(prices)):
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
            
        return max(dp[-1])
