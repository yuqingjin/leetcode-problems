# Method: Recursion
# Basic idea: recursion, from bottom to top return each level's all permutations
# N: length of nums
# Time Complexity: O(∑ k=1 to N *P(N,k)); bcs for each k, need perform N(N-1)...(N-k+1);
# and k is going through the range of value from 1 to N
# Space Complexity: O(N!)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # need to return back the permutation list at the bottom
        if len(nums) == 1:
            # print("leaf node", nums)
            return [nums.copy()]
        
        for i in range(len(nums)):
            cur = nums.pop(0)
            perms = self.permute(nums)
            
            # for example, our return is [[2,3], [3,2]]
            for perm in perms:
                perm.append(cur)

            # 因为res是作为返回值，每次返还给上一层的，所以perms加完可以直接extend进res中；
            # 此时的res还不是最终return的结果
            res.extend(perms)
            nums.append(cur)
        
        # pay attention to the return value here
        # 每次返回下一层perms+append(本层cur)的结果
        return res
                
                
                
            
        
                
