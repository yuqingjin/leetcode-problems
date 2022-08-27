# Method: heapq
# T: O(NlogK)
# S: O(N + k)

from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # method1: heapq
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

        if k == len(nums):
            return nums

        count = Counter(nums)
# heapq.nlargest: Return a list with the n largest elements from the dataset defined by iterable.
        return nlargest(k, count.keys(), key = count.get)
