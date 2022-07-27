# Method: backtracking/DFS/Recursion tree
# T: target value
# M: minimal value in candiates
# N: length of candiates
# Time: O(n*2^n), way too loose; the total height(recursion tree) of all valid result
# Space: O(T/M); when keep adding the smallest element to the combination

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        
        # Basic Idea: choose or not choose the current num
        # i: current index
        def backtracking(i, subset, cur_sum):
            
            # base condition1: reach leaf node and satisfy the requirement
            if cur_sum == target:
                res.append(subset.copy())
                return
            
            # base condition2: reach leaf node and NOT satisfy the requirement
            if i>=len(candidates) or cur_sum > target:
                return
            
            # include current num
            subset.append(candidates[i])
            backtracking(i, subset, cur_sum + candidates[i])
            
            # NOT include current num, skip this 
            subset.pop()
            backtracking(i+1, subset, cur_sum)

        backtracking(0, subset, 0)
        return res
                
                
