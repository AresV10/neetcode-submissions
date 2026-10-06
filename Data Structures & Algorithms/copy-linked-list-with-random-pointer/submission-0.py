"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        dummy = tail = Node(0)
        old_new_mapping = {}    
        while curr:
            tail.next = new_node = old_new_mapping.get(curr, Node(curr.val))
            old_new_mapping[curr] = new_node
            if curr.random in old_new_mapping:
                new_node.random = old_new_mapping[curr.random]
            elif curr.random:
                new_node.random = old_new_mapping[curr.random] = Node(curr.random.val)
            else:
                new_node.random = None
            tail = tail.next
            curr = curr.next

        return dummy.next