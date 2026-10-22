# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pointer = [0]
        val_index = {}
        for i, val in enumerate(inorder):
            val_index[val] = i
        def build(left, right):
            if(left == right):
                return None
            node = TreeNode(preorder[pointer[0]])
            mid = val_index[preorder[pointer[0]]]
            pointer[0]+=1
            node.left = build(left, mid)
            node.right = build(mid+1, right)
            return node
        return build(0, len(preorder))

