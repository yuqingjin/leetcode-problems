# Method: BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        res = []
        
        while q:
            length = len(q)
            sum_value = 0
            for i in range(length):
                cur = q.pop(0)
                sum_value += cur.val

                if cur.left != None:
                    q.append(cur.left)
                    
                if cur.right != None:
                    q.append(cur.right)
            res.append(sum_value/length)
        
        return res
