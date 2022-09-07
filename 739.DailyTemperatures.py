# Method: monotonical stack
# T: O(N)
# S: O(N)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # maintain a non-increasing stack
        stack = []
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                cur_idx = stack.pop()
                res[cur_idx] = i-cur_idx
            stack.append(i)
        
        return res
