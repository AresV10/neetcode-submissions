# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        dummy.next = tail.next = l1
        carry = 0
        while tail.next and l2:
            tail = tail.next
            curr_sum = tail.val + l2.val + carry
            carry, tail.val = divmod(curr_sum,10)
            l2 = l2.next
        if l2:
            tail.next = l2
        while tail.next and carry != 0:
            tail = tail.next
            curr_sum = tail.val + carry
            tail.val = curr_sum % 10
            carry = curr_sum // 10
        if carry:
            tail.next = ListNode(carry)
            
        return dummy.next