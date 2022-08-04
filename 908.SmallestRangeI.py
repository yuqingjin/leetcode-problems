# Method: greedy(?)
# Basic idea: first get the largest difference in this array, max-min; if largest diff is between [0, 2k], then it would turn to zero after adjusting the array; else, the largest diff would decrease to (largestDiff - 2*k)
# Time: O(NlogN)
# Space: O(1)

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        
        nums.sort()
        left = nums[0]
        right = nums[-1]
        
        
        if right - left > 2*k:
            return right-left-2*k
        
        else:
            return 0
