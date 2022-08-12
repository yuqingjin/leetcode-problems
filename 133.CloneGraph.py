# Method: DFS, 
# Basic idea: clone the node and recursively clone its neighbors, until its neighbor have already been cloned; then return back the cloned node,
# T: O(N+M), N: num of nodes, M: num of edges
# S: O(N)

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
                
            return copy
        
        # edge case: when input node is none
        return dfs(node) if node else None
