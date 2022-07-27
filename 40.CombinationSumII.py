# Method: backtracking, DFS
# n: length of nums; have 2^n num of subsets
# Time Complexity: O(2^n); bcs need to consider that 
# each number is either included or excluded in a combination.
# Space Complexity: O(n), the worst case, sum of candidates is equal to target

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        # state variable: i-current index; cur_res-current subset; total-current sum
        def dfs(i, cur_res, total):
            
            # Base case 1: satisfy the reqirement, append to res
            # 先判断是否相等，append进res的情况应该先于逸出/total过大的情况写；
            if total == target:
                res.append(cur_res.copy())
                return
            
            # Base case 2: NOT satisfy the reqirement
            # (no more ele to append to OR total larger than target)
            if i >= len(candidates) or total > target:
                return
            
            # Case1: include into current res
            cur_res.append(candidates[i])
            dfs(i+1, cur_res, total + candidates[i])
            cur_res.pop()
            
            # Case2: NOT include into current res
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, cur_res, total)
        
        
        dfs(0, [], 0)
        return res
            
