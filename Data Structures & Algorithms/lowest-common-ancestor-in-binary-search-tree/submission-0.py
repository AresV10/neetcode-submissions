# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #pick one side, search for number, if 0 go other side, if 1 return, if 2 go down that path
        num_left = self.contains(root.left, p, q) 
        num_right = self.contains(root.right, p, q) 
        if num_left == 1 and num_right == 1 or num_left + num_right == 1:
            return root
        elif num_left == 2:
            print('left')
            return self.lowestCommonAncestor(root.left, p, q)
        elif num_right == 2:
            print('right')
            return self.lowestCommonAncestor(root.right, p, q)

    def contains(self,root: TreeNode, p: TreeNode, q: TreeNode) -> int:
        if not root:
            return 0
        if root.val == p.val or root.val == q.val:
            return 1 + self.contains(root.left, p,q) + self.contains(root.right, p,q)
        else:
            return self.contains(root.left, p,q) + self.contains(root.right, p,q)
        
