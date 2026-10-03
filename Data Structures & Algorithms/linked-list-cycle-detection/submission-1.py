# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        step1 = step2 = head
        if not head or not head.next:
            return False
        step2 = head.next
        while step1!=step2:
            if not step2 or not step2.next:
                return False
            step1 = step1.next
            step2 = step2.next.next

        return True