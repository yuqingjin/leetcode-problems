# Method: hashmap
# Time Complexity: O(n); n: length of nums
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = defaultdict(int)
        
        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in hashmap:
                return [hashmap[diff], i]
            
            # must add to hashmap after the if statement
            hashmap[num] = i 
                
