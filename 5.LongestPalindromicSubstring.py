# Method: DP + 分类讨论
# Basic idea: from a center letter of a substring to validate if its left and right letters are the same 
# Two cases needed to be considered: even or odd length palindrome
# T: O(N^2)
# S: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        max_length = 0
        
        # odd length palindrome
        for i in range(len(s)):
            l = r = i
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-1 > max_length:
                max_length = r-l-1
                res = s[l+1:r]
                
        # even length palindrome
        for i in range(len(s)-1):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-1 > max_length:
                max_length = r-l-1
                res = s[l+1:r]
        return res
