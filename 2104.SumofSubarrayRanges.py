# Method: monotonical stack
# Basic idea: find the num of times that each element acting as minimum value and maximum value
# the num of times as maximum value = num * (i - prev_index) * (prev_index - prev_prev_index)
# T: O(n)
# S: O(n)
    
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        stack = []
        res = 0 
        
        # 1. compute the maximum values
        # the index of maximum value store in stack
        for i, num in enumerate(nums+[inf]):
            # top of the stack is the maximum value
            while stack and nums[stack[-1]] < num:
                print("stack", stack)
                cur_index = stack.pop()
                res += nums[cur_index] * (i-cur_index) * (cur_index-(stack[-1] if stack else -1))
                print("last ele in stack", stack[-1] if stack else None)
                print(res)
            stack.append(i)
        
        stack = []
        
        # 2. compute the minimum values
        for i, num in enumerate(nums + [-inf]):
            # top of the stack is the minimum value
            while stack and nums[stack[-1]] > num:
                print("stack", stack)
                cur_index = stack.pop()
                res -= nums[cur_index]*(i-cur_index)*(cur_index-(stack[-1] if stack else -1))
                print("last ele in stack", stack[-1] if stack else None)
            stack.append(i)
        
        return  res
    
    
#         method 1: 同时维护两个monotonical queue（tle）
#         incQ = []
#         decQ = []
#         res = []
#         l = r = 0
        
#         while l <= r and r < len(nums):
#             while incQ and incQ[-1] >= nums[r]:
#                 incQ.pop()
                
#             while decQ and decQ[-1] <= nums[r]:
#                 decQ.pop()
                
#             incQ.append(nums[r])
#             decQ.append(nums[r])
            
#             res.append(decQ[0] - incQ[0])
#             # print("res", res)
#             r += 1
            
#             if r == len(nums):
#                 l += 1
#                 r = l
#                 incQ = []
#                 decQ = []
#         #     print("subarray", nums[l:r+1])
#         # print("final res", res)
#         return sum(res)
