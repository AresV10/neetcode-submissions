# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (not p and q):
            return False
        if not (p or q):
            return True
        left_res = self.isSameTree(p.left, q.left) 
        right_res = self.isSameTree(p.right, q.right)
        return (p.val==q.val) and left_res and right_res

