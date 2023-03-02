# Method: sliding window + hashmap
# Time: O(S+T);  S-length of s, T-length of t
# Space: O(26)

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        dict_s = Counter(s)
        match = 0
        min_length = float("inf")
        t_length = len(dict_t)

        res = ""
        l = 0

        # expand right boundary
        for r in range(len(s)):
            dict_t[s[r]] -= 1
            if dict_t[s[r]] == 0:
                match += 1
            
            # moving the left boundary
            while match == t_length:
                if min_length > r-l+1:
                    res = s[l:r+1]
                    min_length = r-l+1
                dict_t[s[l]] += 1
                if dict_t[s[l]] > 0:
                    match -= 1
                l += 1

        return res
