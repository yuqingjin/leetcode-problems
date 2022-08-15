# Method: hashmap
# T: O(n), n-length of string s
# S: O(n)
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)
        
        for char in s:
            hashmap[char] += 1
            
        
        for char in t:
            hashmap[char] -= 1
            if hashmap[char] == 0:
                del hashmap[char]

        return len(hashmap) == 0
