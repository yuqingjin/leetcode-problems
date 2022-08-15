# Method: dp
# N: the length of string s, M: max num of word with the same length, M <= 1000
# T: O(20*N*M)
# S: O(N)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp
        s_length = len(s)
        hashmap = defaultdict(set)
        
        for word in wordDict:
            word_len = len(word)
            hashmap[word_len].add(word)
        
        # definition of dp: is the s[:i] in this 
        length = hashmap.keys()
        dp = [False] * (s_length + 1)
        dp[0] = True
        
        for i in range(1, s_length+1):
            for j in length:
                if (i - j) >= 0:
                    # print(s[i:i+j])
                    dp[i] = ((dp[i-j] and s[i-j:i] in hashmap[j])  or dp[i])
                    # print(dp[i])
        
        return dp[-1]
        
        
        
        
#         方法1：dp
#         string_length = len(s)
#         dict_length = len(wordDict)
#         dp = [False for i in range(string_length+1)]
#         dp[0] = True
        
#         # 外层s中的每个元素
#         for i in range(1, string_length+1):
#             for j in range(len(wordDict)):
#                 l = len(wordDict[j])
#                 if i >= l:
#                     dp[i] = dp[i] or (dp[i-l] and wordDict[j] == s[i-l:i]) # 注意此处s的index范围，因为index是从0-string_length的，所以不需要+1了
#                     # print("wordlist: ", wordDict[j])
#                     # print("string: ", s[i-l:i])
#                     # print(dp)
#         return dp[-1]






#         方法2：回溯
#         len_s = len(s)
#         memo = {}
        
#         def backtracking(i):
            
#             # 回溯的终止条件：遍历到s的最末尾
#             if i == len_s:
#                 # res.append(string)
#                 return True
            
#             if i in memo:
#                 return memo[i]
            
#             for word in wordDict:
#                 # print(word)
#                 n = len(word)
#                 if i+n > len_s:
#                     continue
                
#                 # 同时把这两个条件摆在这里，这样才能output出来
#                 if s[i:i+n] == word and backtracking(i+n):
#                     memo[i] = True
#                     print(memo)
#                     return True
                
#             memo[i] = False # 说明这个位置及往后的部分都没办法组成单词
#             print(memo)
#             return False
        
#         return backtracking(0)
