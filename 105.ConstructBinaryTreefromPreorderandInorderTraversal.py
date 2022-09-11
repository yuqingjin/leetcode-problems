# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder):
            
            # end situation: cannot be divided any more
            if not preorder or not inorder:
                return 
            
            # 1.build a new tree root, val = preorder[0]
            root_val = preorder[0]
            root = TreeNode(val = root_val)
            
            # 2.find the sepearate index in inorder array
            root_idx = inorder.index(root_val)
            
            # 3.divide inorder array into left and right parts
            in_left = inorder[:root_idx]
            in_right = inorder[root_idx+1:]
            
            # 4.divide preorder array into left and right parts; 
            # left part size is equal to the inorder left array size
            pre_left = preorder[1:1+len(in_left)]
            pre_right = preorder[1+len(in_left):]

            # 5.recursion
            root.left = dfs(pre_left, in_left)
            root.right = dfs(pre_right, in_right)
            
            # return the root treenode everytime
            return root
        
        
        root = dfs(preorder, inorder)
        return root
            
