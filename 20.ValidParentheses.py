# Method: stack + hashmap
# T: O(n)
# S: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        for p in s:
            
            if p not in hashmap:
                stack.append(p)
                
            else:
                if stack and stack.pop() == hashmap[p]:
                    continue
                    
                else:
                    return False
                
        return stack == []
