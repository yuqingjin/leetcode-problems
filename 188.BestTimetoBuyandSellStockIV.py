# Method: dp
# Time: O(N)
# Space: O(N)

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        # edge case: prices is empty
        if not prices:
            return 0
        
        dp = [[0]*(2*k+1) for i in range(len(prices))]
        
        for i in range(1, 2*k+1, 2):
            dp[0][i] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(1, 2*k+1):
                if j % 2 == 1:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] - prices[i])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + prices[i])
                    
        return max(dp[-1])
