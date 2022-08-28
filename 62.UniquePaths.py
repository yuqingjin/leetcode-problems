# Method: DP
# T: O(N*M)
# S: O(N*M)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 初始化为 1 是因为从(0,0)到(0,i)/(i,0)都是1种方法
        dp = [[1]* (n) for _ in range(m)]
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[-1][-1]
