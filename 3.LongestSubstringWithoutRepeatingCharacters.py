# Method: sliding window
# Time: O(2N) = O(N)
# Space: O(min(m, n)); m:size of the string, n:size of the CharSet

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # set to store all the char in this substring
        l, r = 0, 0
        CharSet = set()
        res = 0
        
        for _ in range(len(s)):
            
            # 将旧index及之前的所有字符删掉
            while s[r] in CharSet:
                CharSet.remove(s[l])
                l +=1 
            
            CharSet.add(s[r])
            res = max(res, r-l+1)
            r+=1
        
        return res
