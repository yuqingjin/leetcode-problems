# Method: dp
# Time: O(N)
# Space: O(N)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # define dp: hold or not hold
        dp = [[0,0] for i in range(len(prices))]
        
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        
        # hold: last time hold, or this time buy in
        # not hold: last time not hold, or this time sell out
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        
        # print(dp)
        return max(dp[-1])
