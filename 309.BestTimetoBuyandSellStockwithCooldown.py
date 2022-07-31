# Method: dp
# Time: O(N)
# Space: O(N)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0, 0] for i in range(len(prices))]
        dp[0] = [-prices[0], 0, 0]
        
        for i in range(1, len(prices)):
            # buy stock: buy it on today(after cooldown), or keep yesterday's hold
            dp[i][0] = max(dp[i-1][2]-prices[i], dp[i-1][0])
            # sell stock: sell it on today or keep yesterday's status
            dp[i][1] = max(dp[i-1][0]+prices[i], dp[i-1][1])
            # cooldown: keep yesterday's cooldown, or cooldown due to yesterday's sell stock
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        
        return max(dp[-1])
