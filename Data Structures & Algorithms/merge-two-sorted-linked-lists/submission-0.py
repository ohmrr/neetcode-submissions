# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next

            curr = curr.next

        while l1:
            curr.next = ListNode(l1.val)
            l1, curr = l1.next, curr.next

        while l2:
            curr.next = ListNode(l2.val)
            l2, curr = l2.next, curr.next

        return dummy.next