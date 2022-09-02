# Method: sort/set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # method 2: set; T: O(N-2N); S: O(N)
        nums_set = set(nums)
        max_length = 0
        
        for num in nums_set:
            # confirm this is the beginning of the consecutive sequence
            if num-1 not in nums_set:
                cur_length = 1
                while num + 1 in nums_set:
                    cur_length += 1
                    num += 1
                max_length = max(max_length, cur_length)
            
        return max_length
        
#         # method 1: sort, T: O(NlogN), S: O(1)
#         if not nums:
#             return 0
        
#         nums = list(set(nums))
#         max_length = 1
#         length = 1
#         nums.sort()
        
#         for i in range(1, len(nums)):
#             if nums[i] - nums[i-1] == 1:
#                 length += 1
#                 max_length = max(max_length, length)
#             else:
#                 length = 1

#         return max_length

    
                
