# Method: backtracking/DFS
# T: O(2^(2n)/(n)^0.5)
# S: O(n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(left, right, cur):
            # 终止条件：用完所有括号
            if left == 0 and right == 0:
                res.append(cur)
                return
            
            # 加左括号的条件：剩余的左括号>0
            if left > 0:
                dfs(left-1, right, cur+"(")
            
            # 加右括号的条件：剩余的右括号多于左括号
            # 防止出现 ")))" 的情况
            if right > left:
                dfs(left, right-1, cur+")")
                
        dfs(n, n, "")       
        return res
