# Method: dp, 完全背包（每种硬币数量不限）
# 求所有组合数，所以遍历顺序为：外层遍历物品，内层遍历背包
# T: O(m*n), m-len(coins), n-amount
# S: O(n)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        # 凑成面额为0的方法有1种
        dp[0] = 1
        
        # 求组合数，所以外层遍历物品，内层遍历背包
        for coin in coins:
            for i in range(coin, amount+1):
                    dp[i] += dp[i-coin]
                    
        return dp[-1]
