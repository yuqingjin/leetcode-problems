# Method: dp
# Basic idea: need to focus on positive negative and zeros. 
# In order to keep track of the negative product, we need to keep track of the cur_min. 
# If zero appears, need to reset cur_min and cur_max to 1. all the subarray include 0, turn to be zero.
# T: O(N)
# S: O(1), no need to keep an array to store the value for dp
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        res = max(nums)
        cur_max = cur_min = 1
        
        # if meet zero, reset cur_max and cur_min to 1
        for i in range(len(nums)):
            
            if nums[i] != 0:
                temp = cur_max
                cur_max = max(nums[i], cur_max*nums[i], cur_min*nums[i])
                cur_min = min(nums[i], temp*nums[i], cur_min*nums[i])
                res = max(res, cur_max)
            else:
                cur_max = cur_min = 1
                
        return res
