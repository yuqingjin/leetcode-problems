# Method: two-pointers + greedy
# Basic idea: facing down the largest value token, and facing up the smallest value token 
# T: O(NlogN), S: O(N)

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if len(tokens) == 1:
            return 1 if power >= tokens[0] else 0
        
        res = 0
        score = 0
        tokens = sorted(tokens)
        l, r = 0, len(tokens)-1
        
        while l < r:
            # gaining scores
            while power >= tokens[l]: 
                score += 1
                power -= tokens[l]
                l += 1
            res = max(res, score)
             
            # when power is not enough for gain score    
            while score >= 1 and power < tokens[l] and l < r:
                score -= 1
                power += tokens[r]
                r -= 1
            
            # if cannot obtain scores from both ways
            if res == 0:
                break
            
        return res
                
                
