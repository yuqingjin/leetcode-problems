# Method: recursive
# T: O(N), N-num of nodes in tree
# S: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            
            if not node or node == p or node == q:
                return node
            
            # left&right不一定是有数值的，可能是None
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 有哪边传哪边
            if not left and right:
                return right
            
            if not right and left:
                return left
            
            # 如果都有，则说明找到了目标node
            if left and right:
                return node
        
        return dfs(root)
 
