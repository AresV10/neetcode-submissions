# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        heap = []
        counter = count()
        heap.append((-1,next(counter), root))
        curr_max = 0
        while heap:
            depth, _,node = heapq.heappop(heap)
            curr_max = depth if depth < curr_max else curr_max
            if node.left:
                heapq.heappush(heap, (depth-1, next(counter), node.left))
            if node.right:
                heapq.heappush(heap, (depth-1, next(counter), node.right))
        return -curr_max




