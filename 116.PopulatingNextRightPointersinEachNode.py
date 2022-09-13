"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# Method: BFS, level order traversal
# T: O(N)
# S: O(N)

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return root
        
        q = [root]
        
        while q:
            length = len(q)
            for i in range(length):
                cur = q.pop(0)
                if i != length - 1:
                    cur.next = q[0]
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                    
        return root
