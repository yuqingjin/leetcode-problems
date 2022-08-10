# Method: DP
# T: O(12*N)
# S: O(N)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # 这两个特殊情况也涵盖在下面的for loop中了，也可以省略
        # 这个写在下面的那个前面
        if amount == 0:
            return 0
        
        # when there is no way to break up the amount
        if amount < min(coins):
            return -1
        
        coins.sort()
        dp = [inf] * (amount+1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[-1] if dp[-1] != inf else -1
        
