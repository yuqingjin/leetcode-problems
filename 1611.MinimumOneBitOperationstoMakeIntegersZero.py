# Method: math
# T: O(logN)
# S: O(1)
    
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        
        res = 0
        while n:
        # ^: Sets each bit to 1 if only one of two bits is 1
            res ^= n
            n //= 2
            
        return res
