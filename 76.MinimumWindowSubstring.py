# Method: sliding window + hashmap
# Time: O(S+T);  S-length of s, T-length of t
# Space: O(26)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_dict = collections.Counter(t)
        # print(t_dict)
        t_length = len(t_dict)
        match = 0
        min_length = inf
        res = ''
        
        l = 0
        m, n = len(t), len(s)
        
        if m > n:
            return ''
        
        for r in range(len(s)):
            t_dict[s[r]] -= 1
        
            if t_dict[s[r]] == 0:
                match +=1
                
            while match == t_length: 
                if min_length > r-l+1:
                    res = s[l:r+1]
                    min_length = r-l+1
                t_dict[s[l]] += 1
                if t_dict[s[l]] > 0:
                    match -= 1
                l+=1
            
        return res
