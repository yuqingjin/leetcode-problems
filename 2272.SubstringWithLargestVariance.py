# Method: Unknown
# Basic idea: the core of largest variance is to find the variance beteen two letters' occurance, so we build array to define each letter with every other letter's occurance
# diff is for store the difference and diff_with_b is for store difference with the existence of B
# Time: O(n*26)
# Space: O(26^2)
# ref: https://leetcode.cn/problems/substring-with-largest-variance/solution/by-endlesscheng-5775/

class Solution:
    def largestVariance(self, s: str) -> int:
        if s.count(s[0]) == len(s):
            return 0
        
        res = 0
        diff = [[0] *26 for i in range(26)]
        diff_with_b = [[-inf] *26 for i in range(26)]
        
        for ch in s:
            a = ord(ch) - ord("a")
            
            for b in range(26):
                if b == a:
                    continue
                    
                diff[a][b] += 1
                diff_with_b[a][b] +=1
                
                diff[b][a] -=1
                diff_with_b[b][a] = diff[b][a]
                
                # havent met b yet, so set diff to 0 and diff_with_b remain negative
                if diff[b][a] < 0:
                    diff[b][a] = 0
                res = max(res, diff_with_b[a][b], diff_with_b[b][a])
                    
        return res

        

          # 暴力解法     
#         res = set()
#         max_var = 0
#         d = defaultdict(int)
        
#         def dfs(i, d):
            
#             if i == len(s):
#                 return 
            
#             for j in range(i, len(s)):
#                 substring = s[i:j+1]
#                 d[s[j]] += 1
#                 if len(d) >=2 and substring not in res:
#                     # print(d)
#                     nonlocal max_var
#                     max_var = max(max_var, max(d.values()) - min(d.values()))
#                     # print(max_var)
#                 res.add(substring)
            
#             d = defaultdict(int)
#             dfs(i+1, d)
                
#         dfs(0, d)
        
#         return max_var
            
                
                
