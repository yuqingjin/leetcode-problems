# Method: DP, 01背包
# T: O(N*capacity)
# S: O(N*capacity)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         重写一遍
        total = sum(nums)
        
        if abs(total) < abs(target):
            return 0
        
        # 不能被分为正负两部分的情况：不存在sum成target的情况
        if (total + target) % 2 == 1:
            return 0
        
        pos = (total + target) // 2 
        neg = (total - target) // 2 
        
        capacity = min(pos, neg)
        
        dp = [[0] * (capacity+1) for _ in range(len(nums)+1)]
        dp[0][0] = 1
        
        for i in range(1, len(nums)+1):
            for j in range(capacity+1):
                dp[i][j] = dp[i-1][j]
                
                # (j-nums[i-1])这部分的capacity是存在的
                if j - nums[i-1] >= 0:
                    # 将capacity中 (j-nums[i-1])这部分的，分给当前的nums[i-1]来占用
                    dp[i][j] += dp[i-1][j-nums[i-1]]
        
        return dp[-1][-1]
                    
        
#         total = sum(nums)
#         if (total + target) % 2 == 1:
#             return 0
        
#         if abs(total) < target:
#             return 0
        
#         # positive part and negative part contribute to the entire target value
#         # 目的: 让一部分数加和为pos， 另一部分加和为neg
#         pos = (total + target) // 2
#         neg = (total - target) // 2
        
#         # capacity 定义为pos&neg中较小的那个数
#         capacity = min(pos, neg)
        
#         # 将问题转化为装满capacity的背包有几种方法
#         # 即组合问题，外层遍历物品，内层遍历背包
#         # dp数组定义：从前i个数字中选取，得到总和为j的方法数
#         dp = [[0] * (capacity + 1) for _ in range(len(nums)+1)]
#         dp[0][0] = 1
        
#         for i in range(1, len(nums)+1):
#             for j in range(capacity+1):
#                 # 对于每个数字(nums[i])，都需要完成选or不选的决定
#                 # 如果当前capacity有空间放nums[i]
#                 if j - nums[i-1] > 0:
#                     # 等于继承前面的+放新的nums[i]
#                     dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                
#                 # 如果没有capacity放nums[i]，直接继承前一种的capacity能凑成的方法数
#                 else:
#                     dp[i][j] = dp[i-1][j]
                
#         return dp[-1][-1]
                    
        
        
#         Method 1: backtracking(TLE)
#         res = 0
#         def backtracking(start, cur_sum):
#             if start == len(nums):
#                 if cur_sum == target:
#                     nonlocal res
#                     res += 1
#                 return
            
#             cur_sum += nums[start]
#             backtracking(start+1, cur_sum)
            
#             cur_sum -= 2*nums[start]
#             backtracking(start+1, cur_sum)
            
#         backtracking(0, 0)    
#         return res

