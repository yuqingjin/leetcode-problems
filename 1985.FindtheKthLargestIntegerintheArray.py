# Method: heapq/quicksort(TLE)
# T: O(N + KlogN)
# S: O(N)

import random
from heapq import *
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        # method 1: quicksort, TLE
#         def partition(lo, hi, pivot):
#             pivot_val = int(nums[pivot])
#             store_index = lo
            
#             nums[hi], nums[pivot] = nums[pivot], nums[hi]
            
#             for i in range(lo, hi):
#                 if int(nums[i]) < pivot_val:
#                     nums[store_index], nums[i] = nums[i], nums[store_index]
#                     store_index += 1
                    
#             nums[hi], nums[store_index] = nums[store_index], nums[hi]
                    
#             return store_index
            
            
#         def select(lo, hi, target):
            
#             if lo == hi:
#                 return nums[lo]
            
#             pivot = random.randint(lo, hi)
#             pivot_index = partition(lo, hi, pivot)
            
#             if pivot_index == target:
#                 return nums[pivot_index]
            
#             elif pivot_index > target:
#                 return select(lo, pivot_index - 1, target)
            
#             else:
#                 return select(pivot_index + 1, hi, target)
            
            
#         return select(0, len(nums)-1, len(nums)-k)



            # method 2: heapq
        heapqueue = []
        for num in nums:
            heappush(heapqueue, -int(num))
        
        for i in range(k):
            cur = heappop(heapqueue)
            
        return str(-cur)
            
            
            
