# Method: math

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        s = str(abs(x))
        s = s[::-1]
        res = int(s) * sign
        
        return res if res in range(-2**31, 2**31) else 0
