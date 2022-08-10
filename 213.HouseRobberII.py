# Method: dp + 分类讨论
# T: O(N)
# S: O(N)
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        # case1: choose the first house, not choose the last house
        dp = [0] * len(nums)
        dp[0] = dp[1] = nums[0]
        
        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        a = dp[-2]
        
        # case2: choose the last house, not choose the first house
        # 应该倒序遍历
        dp = [0] * len(nums)
        dp[-1] = nums[-1]
        dp[-2] = max(nums[-1],nums[-2])
        
        for i in range(len(nums)-3, 0, -1):
            dp[i] = max(dp[i+2]+nums[i], dp[i+1])
        
        b = dp[1]
        
        # case3: neither choose the first or the last
        dp = [0] * len(nums)
        dp[0], dp[1] = 0, nums[1]
        
        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        c = dp[-1]
        
        return max(a,b,c)
