# T: O(N)
# S: O(1)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i, j = 0, 0
        res = []
        
        for k in range(n):
            i += 1
            j += 1
            
            if i == 3 and j == 5:
                res.append("FizzBuzz")
                i, j = 0, 0
                
            elif i == 3:
                res.append("Fizz")
                i = 0
                
            elif j == 5:
                res.append("Buzz")
                j = 0
                
            else:
                res.append(str(k+1))
                
        return res
