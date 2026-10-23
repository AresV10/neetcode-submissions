# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 'None'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        pointer = [0]
        def deserialize_help():
            if arr[pointer[0]] == 'None':   
                pointer[0]+=1
                return None
            root = TreeNode(int(arr[pointer[0]]))
            pointer[0]+=1
            root.left = deserialize_help()
            root.right = deserialize_help()
            return root
        return deserialize_help()






