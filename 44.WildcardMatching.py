# Method: DP
# T: O(m*n)
# S: O(m*n)
    
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s)+1)]
        
        # 初始化dp[0][0]，空字符匹配空字符
        dp[0][0] = True     
        
        # 初始化dp[0][i]，如果p的前j个字符为*，空字符和这段substring匹配
        for i in range(1, len(p)+1):
            if p[i-1] == "*":
                dp[0][i] = True
            else:
                break
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                if p[j-1] == "?" or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                          
        return dp[-1][-1]
        
