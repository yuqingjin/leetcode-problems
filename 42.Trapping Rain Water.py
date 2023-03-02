class Solution:
    def trap(self, height: List[int]) -> int:
        # method: stack
        # basic idea: maintain the non increasing stack; and pop up ele from top of stack until the new element no longer larger than ele from top of the stack
        # store the index in stack
        res = 0
        stack = []
        i = 0

        while i < len(height):
            while stack and height[i] > height[stack[-1]]:
                mid = stack.pop()
                if stack:
                    h = min(height[i], height[stack[-1]]) - height[mid]
                    w = i - stack[-1] - 1
                    res += h*w
            stack.append(i)
            i += 1

        return res


        # method: dp
        dp = [0] * len(height)
        l_max, r_max = height[0], height[-1]

        if len(height)<=1: return 0

        # iterate from left to right
        # and then from right to left to find the minimum
        for i in range(len(height)):
            l_max = max(height[i], l_max)
            dp[i] = l_max - height[i]
        for j in range(len(height)-1, -1, -1):
            r_max = max(height[j], r_max)
            dp[j] = min(dp[j], r_max-height[j])
        
        return sum(dp)
