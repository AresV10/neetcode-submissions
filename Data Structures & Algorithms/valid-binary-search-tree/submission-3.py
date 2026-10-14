# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root,-1000000001,1000000001)

    def helper(self,root: Optional[TreeNode], minimum: int, maximum: int) -> bool:
        if not root:
            return True
        if root.val <= minimum or root.val >= maximum:
            return False
        
        return self.helper(root.left, minimum, root.val) and self.helper(root.right, root.val, maximum)