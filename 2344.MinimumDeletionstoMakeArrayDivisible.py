# method: math
# basic idea: 1.the num should be the common divisor of all the element in numsDivide, 2. sort the nums array to traverse from the smallest to largest

import math
from bisect import *
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        g = math.gcd(*numsDivide)
        # print(g)
        
        res = -1
        for i, num in enumerate(nums):
            if g % num == 0:
                res = i
                break
        
        return res
