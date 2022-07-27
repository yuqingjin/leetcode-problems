# Method: backtracking
# n: length of nums
# Time Complexity: O(n*2^n); bcs need to traversal every subset. 
# There are 2^n numbers of subsets and each subset has n maximum length.
# Space Complexity: O(n); bcs maximum length is n. The most space efficient way to keey subset is only use one array to store subset.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = [] # 只用一个subset来放leaf node的元素
        
        # i is the value we are making decision on
        def backtracking(i):
            # base case: reach to the leaf node
            if i == len(nums):
                res.append(subset.copy()) # return copy bcs subset is adjustable
                return 
            
            # case1: include this number in subset
            subset.append(nums[i])
            backtracking(i+1)
            
            # case2: NOT include this number in subset
            subset.pop()
            backtracking(i+1)
            
        
        backtracking(0)
        return res
