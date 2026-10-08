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
        node_map = {}
        dummy = Node(0)
        original = head
        curr = dummy

        while original:
            curr.next = Node(original.val)
            node_map[original] = curr.next
            original = original.next
            curr = curr.next

        original = head
        curr = dummy.next

        while curr:
            curr.random = node_map[original.random] if original.random else None
            original = original.next
            curr = curr.next

        return dummy.next