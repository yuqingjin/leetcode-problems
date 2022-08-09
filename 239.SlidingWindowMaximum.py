# Method: sliding window + queue(monotonical decreasing queue)
# Time: O(n)
# Space: O(n)
    
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = r = 0
        q = deque()
        res = []
        
        # 先将前k个元素放入deque
        while r-l+1 != k:
            # 重点是把每次大于等于nums[r]的数从右往左都pop出去，最终目的是，把nums[r]放进队列，使他成为q中最右端的数。
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            r+=1
        
        
        # 再开始遍历
        while r < len(nums):
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            r += 1
            res.append(q[0])
            
            if nums[l] == q[0]:
                q.popleft()
            
            l += 1
        
        return res
