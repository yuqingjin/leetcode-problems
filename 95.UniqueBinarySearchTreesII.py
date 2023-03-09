# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Method: backtracking, recursion,
with the definition of BST, if the left subtree is not empty, then every node val in leftsubtree would be smalller than root val; if the right subtree is not empty, then every node val in rightsubtree would be smalller than root val
T: O()
S: O()
ref: https://leetcode.com/problems/unique-binary-search-trees-ii/solutions/1440190/c-python-simple-and-short-recursive-solutions-with-explanation/
'''

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generate(1, n)

    def generate(self, start, end):
        res = []

        # terminaltion condition:
        # 1) start > end: return [None] val
        # 2) start == end: return [TreeNode(val = start)]
        
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(val = start)]

        for i in range(start, end+1):
            left_subtree = self.generate(start, i-1)
            right_subtree = self.generate(i+1, end)

            for left in left_subtree:
                for right in right_subtree:
                    root = TreeNode(val = i)
                    root.left = left
                    root.right = right
                    res.append(root)

        return res
