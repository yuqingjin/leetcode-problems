# Method: sliding window + hashmap
# Time: O(26*N)
# Space: O(1)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count = collections.Counter(s1)
        # print(count)
        
        if len(s1) > len(s2):
            return False
        
        s = len(s1)
        l = 0
        for i in range(s-1):
            count[s2[i]] -= 1

        
        for r in range(l+s-1, len(s2)):
            count[s2[r]] -= 1
            if set(count.values()) == {0}:
                return True
            
            count[s2[l]] += 1
            l += 1
        
        return False
            
        
