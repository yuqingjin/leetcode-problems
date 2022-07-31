# Method: array/dp
# Baic idea: record the minimum price, compute the profit each time and save the maximum one 
# Time: O(N)
# Space: O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # 方法1：array
#         res = 0
#         minimum = prices[0]
        
#         for i in range(1, len(prices)):
#             res = max(res, prices[i]-minimum)
#             minimum = min(minimum, prices[i])
        
#         return res
            
        # 方法2：dp
        
        # dp tuple分别表示第i天持有或不持有股票；
        days = len(prices)
        dp = [[0, 0] for i in range(days)]
        # print(dp)
        
        # 第0天，持有为负，不持有为0
        dp[0] = [-prices[0], 0]
        
        # 持有：今天买入或者保持昨天持有
        # 不持有：今天卖出或昨天就没持有
        for i in range(1, days):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        
        return max(dp[-1])
            
