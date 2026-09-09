# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # curr, length = head, 0
        # while curr:
        #     curr = curr.next
        #     length += 1

        # target = length - n
        # if target == 0:
        #     return head.next

        # curr = head
        # while curr:
        #     if target == 1:
        #         curr.next = curr.next.next
        #         break

        #     curr = curr.next
        #     target -= 1
        
        # return head

        dummy = ListNode(0, head)
        left, right = dummy, head

        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next
