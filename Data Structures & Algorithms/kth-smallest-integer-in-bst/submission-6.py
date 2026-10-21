# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def help(node, index):
            if not node.left and not node.right:
                if k == index+1 : 
                    return (node.val, k)
                return (-1, index+1)
            left_val, right_val, left_index, right_index = 0, 0, index, 0
            if node.left:
                left_val, left_index = help(node.left, index)                
                if left_val >= 0:
                    return (left_val, left_index)
            if left_index+1 == k:
                return (node.val, k)
            if node.right:
                right_val, right_index  = help(node.right, left_index+1)
                if right_val >= 0:
                    return (right_val, right_index)
            #combine counts
            curr_index = right_index if node.right else left_index+1
            return (-1, curr_index)
                    
        return help(root, 0)[0]