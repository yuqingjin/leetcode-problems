# Method: Loop Iteration
# T: O(log3(N))
# S: O(1)
    
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        while n > 1:
            n = n / 3
            if not n.is_integer:
                return False
        
        return n == 1
