# Method: dp or two-pointer
# Basic idea: find the leftMax and rightMax to compute the trapped water amount
# for 2-pointers, we need to shift the lower side of boundary, bcs lower side would determine the amount of water we collect.(the same idea as LC 11.ContainerWithMostWater)
# Time: O(N); O(N)
# Space: O(N); O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        
#         # Method1: dp
#         dp = [0] * len(height)
#         leftMax = height[0]
#         rightMax = height[-1]
        
#         # using leftMax to compute 
#         for i in range(1, len(height)):
#             leftMax = max(leftMax, height[i])
#             dp[i] = leftMax - height[i]
        
#         # using rightMax to compute 
#         for i in range(len(height)-1, 0, -1):
#             rightMax = max(rightMax, height[i])
#             # find the smaller amount of them, 
#             # which is the result considering both leftMax and rightMax
#             dp[i] = min(dp[i], rightMax - height[i])
            
#         return sum(dp)

    
    
        # Method2: Two-pointer
        l, r = 0, len(height)-1
        leftMax = height[0]
        rightMax = height[-1]
        res = 0
        
        # everytime shift the lower side of (leftMax, rightMax)
        while l < r:
            if leftMax < rightMax:
                l += 1
                res = max(res, res + (leftMax - height[l]))
                leftMax = max(leftMax, height[l])
                
            else:
                r -= 1
                res = max(res, res + (rightMax - height[r]))
                rightMax = max(rightMax, height[r])
                
        return res
