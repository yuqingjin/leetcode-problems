# Method: greedy?
# Basic idea: For size N list, the smallest missing positive integer is in [1, N+1]; so we maintain a constant length list to store the occurence from 1 to N+1 in nums.
# T: O(N)
# S: O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        lst = [False] * (size + 2)
        
        for num in nums:
            if num > 0 and num < size+1:
                lst[num] = True
                
        for i in range(1, len(lst)):
            if lst[i] == False:
                return i
