# method: dp
# T: O(N*M)
# S: O(N*M)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # distinct subsequence 需要同时考虑 继承 和 左上/右下角
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        
        # initilization, t的第0位（空），和任一s的字母匹配
        for i in range(len(s)+1):
            dp[i][0] = 1
        
        for i in range(1, len(s)+1):
            for j in range(1, len(t) + 1):
                dp[i][j] = dp[i-1][j]
                
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
                    
        return dp[-1][-1]
