# Method: backtracking
# T: O(N* 4^N), there are 4^N paths, and each path(combination) costs up to N to build the combination.
# S: O(N)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        
        # edge case: no digits in input
        if not digits:
            return res
        
        def backtracking(string, i):
            if i >= len(digits):
                res.append(string)
                return
                
            cur = d[digits[i]]
            
            for j in range(len(cur)):
                string += cur[j]
                backtracking(string, i+1)
                string = string[:-1]
                
        backtracking("", 0)
        # print("res", res)
        return res
            
            
            
