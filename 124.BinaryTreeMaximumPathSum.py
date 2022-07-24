# Method: Recursion
# Time Complexity: O(N), need to traverse all the node
# Space Complexity: O(h), h: height of the tree; because of DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 第二遍自己做
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val] # 如果不初始化为root.val的话，会出现不满足根节点为负的边界情况
        def dfs(root):
            if not root:
                return 0
            
            leftMax = max(0, dfs(root.left))
            rightMax = max(0, dfs(root.right))
            
            # 最终只记录sum最大的有split的一种情况
            res[0] = max(res[0], leftMax + root.val + rightMax)
            
            # 每次返回的是无split的值
            return (root.val + max(rightMax, leftMax))
        
        dfs(root)
        
        return res[0]


#         第一遍
#         res = [root.val]
        
#         def dfs(root):
#             if not root:
#                 return 0
            
#             # make sure left and right max is above 0
#             leftMax = max(dfs(root.left),0)
#             # print("leftMax", leftMax)
#             rightMax = max(dfs(root.right),0)
#             # print("rightMax", rightMax)
            
#             # with Split: 记录在每个节点上有split的情况的sum值；
#             # 该值存在res中，不返回
#             res[0] = max(res[0], leftMax + root.val + rightMax)
#             # print("with split", res[0])
            
#             # without split：每次dfs返回的值，无split的情况
#             # print("without split", root.val + max(leftMax, rightMax))
#             return root.val + max(leftMax, rightMax)
        
#         # 进行递归
#         dfs(root)
#         return res[0] 
#         # 返回有split的值，该值肯定大于无split的情况
#         #（因为leftMax和rightMax都是positive）
            
            
            
        
        
        
        
            
