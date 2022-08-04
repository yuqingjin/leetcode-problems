# Method: greedy algorithm
# Basic Idea: deciding any two adjacent numbers smallest range, and compare it with the most left boundary and the most right boundary
# Time: O(NlogN), to sort the array
# Space: O(1)
    
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxim, minim = nums[-1], nums[0]
        
        res = maxim - minim
        up = maxim - k
        down = minim + k 
        
        for i in range(1, len(nums)):

            # 比较二者中更大的范围区间，和res的差异，取较小值
            res = min(res, max(up, nums[i-1]+k)- min(down, nums[i]-k))
        
        return res
        
