# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # method: folllow the rules of binary search tree
        res = None
        
        while root:
            if root.val > p.val:
                res = root
                root = root.left
            else:
                root = root.right
        return res
        
        # method: DFS
#         res = []
#         def dfs(node):
#             if not node:
#                 return
            
#             dfs(node.left)
#             nonlocal res
#             res.append(node)
#             dfs(node.right)
        
#         dfs(root)
#         for idx, ele in enumerate(res):
#             if ele == p:
#                 break
        
#         res.append(None)
#         return res[idx+1]
