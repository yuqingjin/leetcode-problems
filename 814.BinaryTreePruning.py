# Method: recursion, dfs
# T: O(logN)
# S: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            # 递归到leaf node
            if not node:
                return None
            # 直接在此处重新定义node的左右子节点
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            # 判断删除的子树条件：左右都是空，本身的val是0
            if not node.left and not node.right and node.val == 0:
                return None
            # 最终返回node本身
            return node
        
        return dfs(root)
