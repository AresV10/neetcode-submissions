# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        state = True
        stack = [(p,q)]
        while stack and state:
            left, right = stack.pop()
            if not left and not right:
                state = True
            elif not left or not right:
                state = False
            else:
                state = (left.val == right.val)
                stack.append((left.left, right.left))
                stack.append((left.right, right.right))

        return state
