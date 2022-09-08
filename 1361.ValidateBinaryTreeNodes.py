class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        # Method: Unionfind; T:O(N), O(N)
        # Basic idea: if a binary tree is valid, 1.it has no cycle in it, 2.only one root, 3.traverse every tree nodse via BFS exactly once 
        if n == 1:
            return True
        
        # find the root(there is only one root existing) 
        indegree = [0] * n
        for i in range(n):
            if leftChild[i] != -1:
                indegree[leftChild[i]] += 1
            if rightChild[i] != -1:
                indegree[rightChild[i]] += 1
        
        root = [i for i in range(n) if indegree[i] == 0]
        # print(root)
        if len(root) != 1:
            return False
        
        # find if there is a cycle in the graph(BFS)
        visit = set(root)
        while root:
            length = len(root)
            for i in range(length):
                cur = root.pop(0)
                
                if leftChild[cur] != -1:
                    if leftChild[cur] in visit: return False
                    visit.add(leftChild[cur])
                    root.append(leftChild[cur])
                    
                if rightChild[cur] != -1:
                    if rightChild[cur] in visit: return False
                    visit.add(rightChild[cur])
                    root.append(rightChild[cur])
                    
        # make sure every node traversed once
        return len(visit) == n
        
