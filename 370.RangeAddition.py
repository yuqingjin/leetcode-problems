# Method 2: Range caching
# Time: O(N+k)
# Space: O(1)

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
#         Method 1: Brute force
#         arr = [0] * length
        
#         for update in updates:
#             start, end, inc = update[:]
#             i = 0 
#             while i < end-start + 1:
#                 arr[start+i] += inc
#                 i+=1
        
#         return arr


#         Method 2: Range caching
#         Time: O(N+k)
#         Space: O(N)
        # the last position is only store the cache of arr[length - 1]
        arr = [0] * (length+1)
        
        for update in updates:
            start, end, inc = update[:]
            # cache the start position and the next pos of end
            arr[start] += inc
            arr[end+1] -= inc
        
        for i in range(1, length):
            res[i] += res[i-1]
        
        return arr[:-1]
