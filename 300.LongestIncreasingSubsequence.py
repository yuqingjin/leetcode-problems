# Method: dp/binary search

from bisect import *
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # method: binary search, T: O(NlogN)
        # basic idea: 通过二分法，使单调递增序列缓慢增长
        # ref: https://leetcode.cn/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-he-er-fen-cha-zhao-lian-x7dh/
        q = [nums[0]]
        nums = nums[1:]
        
        for num in nums:
            # 因为q是单调递增的，所以直接判断q中最大值与num的大小关系
            # 确定要append还是replace
            if q and q[-1] < num:
                q.append(num)
            else:
                # bisect_left找的是插入位点，从左开始查找
                idx = bisect_left(q, num)
                q[idx] = num
        return len(q)
        
        
        # method: dp; T:O(N^2)
#         dp = [1] * len(nums)
#         res = 1
        
#         for i in range(1, len(nums)):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j]+1)
#             res = max(res, dp[i])  
#         return res
