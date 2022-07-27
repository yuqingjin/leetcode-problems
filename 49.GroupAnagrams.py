# Method: hashmap
# Time Complexity: O(nlogn*m); n: max length of a single word, 
# m: num of word in strs
# Space Complexity: O(m), at worst

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for word in strs:
            transformed = sorted(list(word))
            transformed = "".join(transformed)
            d[transformed].append(word)
        
        return list(d.values())
