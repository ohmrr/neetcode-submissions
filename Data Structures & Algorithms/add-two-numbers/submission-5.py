# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        dummy = ListNode()
        curr = dummy
        carry = 0

        while n1 or n2 or carry:
            summ = carry

            if n1:
                summ += n1.val
                n1 = n1.next
            
            if n2:
                summ += n2.val
                n2 = n2.next

            curr.next = ListNode(summ % 10)
            curr = curr.next
            carry = summ // 10

        return dummy.next