# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        curr, prev, i = prev, None,1 
        while curr:
            next_node = curr.next
            curr.next = prev
            if i != n:   
                prev = curr
            curr = next_node
            i+=1
        return prev