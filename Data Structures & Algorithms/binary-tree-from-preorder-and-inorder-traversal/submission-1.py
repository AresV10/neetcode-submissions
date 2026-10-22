# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper (Pre_L, Pre_R, In_L, In_R, val_index):
            if Pre_R - Pre_L < 1 or In_R - In_L < 1:
                return None
            root = preorder[Pre_L]
            curr = val_index[root]
            left_size = curr - In_L 
            return TreeNode(root, helper(Pre_L+1,Pre_L + 1 + left_size,In_L,curr,val_index), helper(Pre_L + 1 + left_size,Pre_R,curr+1,In_R, val_index))
        val_index = {}
        for i, val in enumerate(inorder):
            val_index[val] = i
        return helper(0, len(preorder), 0, len(inorder), val_index)

    


