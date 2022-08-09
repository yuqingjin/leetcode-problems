# Method: sliding window + monotonic queue
# T: O(N); if use binary tree, O(NlogN)
# S: O(N)
    
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        l = r = 0
        inc = dec = deque()
        res = 1
        
        while l <=r and r < len(nums):
            # monotonical increasing queue
            while inc and inc[-1] > nums[r]:
                inc.pop()
            inc.append(nums[r])
            
            # monotonical decreasing queue
            while dec and dec[-1] < nums[r]:
                dec.pop()
            dec.append(nums[r])
            
            # adjusting while maxDiff above limit
            while inc and dec and (dec[0] - inc[0]) > limit:
                if nums[l] == dec[0]:
                    dec.popleft()
                elif nums[l] == inc[0]:
                    inc.popleft()
                l += 1
            
            res = max(res, r-l+1)
            r += 1
            
        return res
