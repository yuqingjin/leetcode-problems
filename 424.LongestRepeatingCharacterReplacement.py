# Method: sliding window
# Basic idea: use while loop to delete the left boundary characters in order to keep the replacing num less or equal to k
# Time: O(26N), bcs need to find the maximum values in dict each time
# Space: O(N)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, r = 0, 0
        d = defaultdict(int)
        max_occur = 0
        res = 0
        
        for i in range(len(s)):
            d[s[r]] += 1
            # bcs after adjusting the left pointer, the max_occur character may change to other characters
            max_occur = max(max(d.values()), d[s[r]])
            
            while (r-l+1 - max_occur) > k:
                    d[s[l]] -=1
                    l += 1
                    
            res = max(res, r-l+1)
            r += 1
            
        return res
