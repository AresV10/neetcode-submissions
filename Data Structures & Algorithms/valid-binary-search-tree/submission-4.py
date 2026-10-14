# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def Valid(root, minimum, maximum):
            if not root:
                return True
            if not (minimum < root.val < maximum):
                return False
            return Valid(root.left, minimum, root.val) and Valid(root.right, root.val, maximum)
        return Valid(root,-1000000001,1000000001)