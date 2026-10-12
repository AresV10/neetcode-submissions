# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            node_left, node_right= root.left, root.right
            root.right = self.invertTree(node_left)
            root.left = self.invertTree(node_right)
        return root