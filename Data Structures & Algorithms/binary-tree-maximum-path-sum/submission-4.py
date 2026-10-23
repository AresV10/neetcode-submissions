# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = [float('-inf')]
        def maxSubtreePathSum(node):
            if not node:
                return 0
            left = max(maxSubtreePathSum(node.left),0)
            right =  max(maxSubtreePathSum(node.right),0)
            maxPath[0] = max(maxPath[0], node.val+left+right)
            return node.val + max(left, right)
        maxSubtreePathSum(root)
        return maxPath[0]