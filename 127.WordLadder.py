# Method: BFS graph problem
# Time Complexity: O(n*m^2), n: max length of wordList, m: max length of word
# Space Complexity: O(n*m), because there are at most nm num of pattern in dictionary
    
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        dictionary = defaultdict(list)
        wordList.append(beginWord) # To avoid the situation: beginword not in list
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                dictionary[pattern].append(word)
        wordList.pop() 
        
        q = [beginWord]
        visited = set([beginWord]) # set里面要写中括号
        count = 1
        
        while q:
            
            # 不能写成"for word in q"的形式，因为会不断有元素append进queue；
            # forloop会继续进行。
            for i in range(len(q)):
                word = q.pop(0)
                if word == endWord:
                    return count
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighWord in dictionary[pattern]:
                        if neighWord not in visited:
                            visited.add(neighWord)
                            q.append(neighWord)
        
            count +=1 
        # if could not find endword as the last word sequence, 
        # it means no shortest transformation sequence exists
        return 0
