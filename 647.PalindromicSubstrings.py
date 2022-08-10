# Method: 分类讨论
# Basic idea: expand around possible centers: from a center letter of a substring to validate if its left and right letters are the same 
# T: O(N^2)
# S: O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        # odd length
        for i in range(len(s)):
            l = r = i
            
            while l >= 0 and r < len(s) and s[l]==s[r]:
                l-=1
                r+=1
                res += 1
                
        # even length
        for i in range(len(s)-1):
            l, r = i, i+1
            
            while l >= 0 and r < len(s) and s[l]==s[r]:
                l-=1
                r+=1
                res += 1
        
        return res
