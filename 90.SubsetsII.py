# Method: backtracking
# n: length of nums; have 2^n num of subsets
# Time Complexity: O(n*2^n); bcs need to traversal every element in every subset. 
# There are 2^n numbers of subsets and each subset has n maximum length.
# Space Complexity: O(n); bcs maximum length is n. The most space efficient way to keey subset is only use one array to store subset.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # visit = set()
        res = []
        nums.sort()
        
        def dfs(i, subset):
            # base case: reach to leaf node
            if i == len(nums):
                # can also use visit set to avoid duplicates
                # t = tuple(subset)
                # if t not in visit:
                    # visit.add(t)
                res.append(subset.copy())
                return
            
            # Case 1: include nums[i] into subset
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
            
            # Case 2: NOT include nums[i] into subset
            # e.g.[1,2,2,3] if we are at the first of 2.
            # Bcs we want to skip this num, and the next one is the same value as this; we need to skip both of them to avoid duplicates
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
                
            dfs(i+1, subset)
        
        dfs(0, [])
        return res
            
            
