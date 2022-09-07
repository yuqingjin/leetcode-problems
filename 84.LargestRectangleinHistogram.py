# Method: stack
# Basic idea: find the lower bar on two sides of the higher bar
# T: O(N)
# S: O(N)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # maintain a non-decreasing stack
        # store the index of ele in stack
        stack = [0]
        res = 0
        heights = [0] + heights + [0]
        
        for i in range(1, len(heights)):
            
            # 三种情况：
            # 1、入栈元素大于栈顶元素
            if heights[stack[-1]] < heights[i]:
                stack.append(i)
            
            # 2、入栈元素等于栈顶元素
            elif heights[stack[-1]] == heights[i]:
                stack.pop()
                stack.append(i)
            
            # 3、入栈元素小于栈顶元素
            else:
                # drop all the elements larger than heights[i]
                while stack and heights[stack[-1]] > heights[i]:
                    highest = stack.pop()
    
                    if stack:
                        left = stack[-1]
                        right = i
                        height = heights[highest]
                        width = right - left - 1
                        res = max(res, height*width)
                        
                stack.append(i)
        
        return res
        
        
#         Method 1: T: O(N^2), TLE
#         n = len(heights)
#         max_rect = 0
        
#         for i in range(n):
#             lowest = heights[i]
#             for j in range(i, n):
#                 lowest = min(lowest, heights[j])
#                 if lowest == 0:
#                     break
#                 max_rect = max(max_rect, lowest*(j-i+1))
                
#         return max_rect
