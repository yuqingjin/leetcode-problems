# Method: Backtracking + memorization(with cache)
# Basic idea: find all partitions and validate if they're palidrome
# n: length of the string
# Time: O(n*2^n), the worst case: s include n num of the same letter;
# there are 2^n method to partition and each method need n times.
# Space: O(n)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []
        
        @cache
        def is_Palindrome(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
            
        def backtracking(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                partition.append(s[i:j+1])
                if is_Palindrome(s, i, j):
                    backtracking(j+1)
                partition.pop()
        
            
        backtracking(0)
        is_Palindrome.cache_clear()
        return res
        
            
