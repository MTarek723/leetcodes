# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        checker = head
        while checker is not None and checker.next :
            if checker.next.val == checker.val:
                checker.next = checker.next.next
            else:
                checker = checker.next
        return head