# Method: DP
# T: O(N)
# S: O(N)

class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0
        
        # dp[i]: Ways to decode a string of size i
        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1
        
        for i in range(2, len(s)+1):
            # 先对这一位进行validate，如果不为0，则可以继承前面的decode ways
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            
            # 再对这一位和它前一位组成的两位数进行validate，
            # 如果在[1,26]范围内，则可以继承[i-2]的decode ways
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        # return the num of decode ways of a string of size len(s)
        return dp[-1]      
