# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, prev, fast = head, head, head
        if head.next is None:
            return
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        #reverse  slow - fast
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        #prev is new head for merge
        dummy = tail = ListNode()
        flag = True
        while prev and head:
            if flag:
                tail.next = head
                head = head.next
                flag = False
            else:
                tail.next = prev
                prev = prev.next
                flag = True
            tail = tail.next
        tail.next = head or prev
            
