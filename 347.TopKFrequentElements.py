# Method: heapq, heapq + counter, quicksort

import random
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # method1: heapq
        # T: O(NlogK)
        # S: O(N + k)
#         lst = []
#         hashmap = defaultdict(int)
#         for num in nums:
#             hashmap[num] += 1
            
#         for key, v in hashmap.items():
#             lst.append((-v, key))

#         heapify(lst)
#         res = []
#         for _ in range(k):
#             cur = heappop(lst)
#             res.append(cur[1])
            
#         return res
        
#         method 2: heapq + counter

#         if k == len(nums):
#             return nums

#         count = Counter(nums)
# # heapq.nlargest: Return a list with the n largest elements from the dataset defined by iterable.
#         return nlargest(k, count.keys(), key = count.get)


#         method 3: quicksort
#         T: O(N), average
#         S: O(N)
        count = collections.Counter(nums)
        lst = [(k, v) for k, v in count.items()]
        
        def partition(lo, hi, pivot_index):
            
            store_index = lo
            pivot_val = lst[pivot_index][1]
            
            # place the pivot at the end of the list
            lst[hi], lst[pivot_index] = lst[pivot_index], lst[hi]
            
            # swap the smaller element to the left
            for i in range(lo, hi):
                if lst[i][1] < pivot_val:
                    lst[i], lst[store_index] = lst[store_index], lst[i]
                    store_index += 1
                    
            # place the pivot to its right place, from hi to store_index position
            lst[hi], lst[store_index] = lst[store_index], lst[hi]
            
            return store_index
            
        def select(lo, hi, k): 
            if lo == hi:
                return [lst[i][0] for i in range(lo, len(lst))]
            
            pivot_index = random.randint(lo, hi)
            pivot_pos = partition(lo, hi, pivot_index)

            if pivot_pos == len(lst) - k:
                return [lst[i][0] for i in range(pivot_pos, len(lst))]

            elif pivot_pos < len(lst) - k:
                return select(pivot_pos + 1, hi, k)

            else:
                return select(lo, pivot_pos - 1, k)
        
        return select(0, len(lst)-1, k)
            
