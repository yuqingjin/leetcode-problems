# Method 2: hashmap, prefix table
# Basic idea: compute the prefixSum during the traversal of array nums, everytime traverse one int in array, explore if (target-current_sum) exist in prefixSum table, if it exists, add them to res. And remember to record the cur_sum to hashmap after that.
# Time: O(N)
# Space: O(N)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
#       Method1: Brute force:
#       Time: TLE
#         res = 0
#         def dfs(i):
#             cur_sum = 0
            
#             if i == len(nums):
#                 return
            
#             for j in range(i, len(nums)):
#                 cur_sum += nums[j]
                
#                 if cur_sum == k:
#                     nonlocal res
#                     res += 1
#             dfs(i+1)
                    
#         dfs(0)
#         return res
        
#   Method 2: hashmap, prefix table
#   Time: O(N)
#   Space: O(N)
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        cur_sum = 0
        res = 0
        
        for i, num in enumerate(nums):
            cur_sum += num
            if (cur_sum - k) in prefixSum:
                res += prefixSum[cur_sum - k]
                
            prefixSum[cur_sum] += 1
            
        return res
                
        
        
        
