# Method: Two-Pointer
# Basic idea: shifting the smaller height side, bcs the amoount of water stored is determined by the smaller height side;
# if we shifting the larger height, it is impossible to get more water
# when they are the same, it doesnt matter which side to shift
# Time: O(N)
# Space:O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_water = 0
        
        while l < r:
            cur_water = min(height[l], height[r]) * (r-l)
            max_water = max(max_water, cur_water)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                    
        return max_water
