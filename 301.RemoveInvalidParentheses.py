# Method: backtracking
# Time Complexity: O(2^N), N: num of char in s
# e.g. worst case: s = "((((", need to do two operations under "(" condition
# Space Complexity: O(N), we need to store the result; 
# if no character need to be removed, the maximum length is gained, which is N

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        self.longest_str = -1
        self.cur_res = set()
        
        self.dfs(s, 0, [], 0, 0)
        
        return list(self.cur_res)
    
    # idx: current index; string: make_up string, data type is list;
    # left/right: left/right parentheses count;
    def backtracking(self, s, idx, string, left, right):
        
        # end condition: reach to the end of string
        if idx >= len(s):
            
            # only when left parentheses is equal to right counterpart, the result is valid
            if left == right:
                
                # Because we need to remove minimum parentheses to make it valid; 
                # we need to obtain the longest res.
                # new string longer than the existing current res;
                # it's time to update res
                if len(string) > self.longest_str:
                    self.longest_str = len(string)
                    self.cur_res  = set()
                    self.cur_res.add("".join(string))
                
                # new string is as the same length as existing current res; append to cur_res
                elif len(string) == self.longest_str:
                    self.cur_res.add("".join(string))
        
        # still need to append character 
        else:
            cur_char = s[idx]
            
            if cur_char == "(":
                # skip this character 
                self.dfs(s, idx + 1, string, left, right)
                
                # choose this character 
                string.append(cur_char)
                self.dfs(s, idx + 1, string, left + 1, right)
                string.pop()
                
            elif cur_char == ")":
                # skip this character 
                self.dfs(s, idx + 1, string, left, right)
                
                # can only choose this character when left > right
                if left > right:
                    string.append(cur_char)
                    self.dfs(s, idx + 1, string, left, right + 1)
                    string.pop() 

            else:
                # choose this character: must include letters in res
                string.append(cur_char)
                self.dfs(s, idx + 1, string, left, right)
                string.pop()
            
