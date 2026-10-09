# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        counter = count()
        dummy = tail = ListNode()
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, next(counter), node))
        # min heap loaded up
        while heap:
            curr_node = heapq.heappop(heap)[2]
            tail.next = curr_node
            if curr_node.next:
                heapq.heappush(heap, (curr_node.next.val, next(counter), curr_node.next))
            tail = tail.next
        return dummy.next


