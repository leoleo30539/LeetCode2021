# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            cur = l1
            l1 = l1.next
        else:
            cur = l2
            l2 = l2.next
        head = cur
        prev = head
        while l1 and l2:
            if l1.val < l2.val:
                cur = l1
                l1 = l1.next
            else:
                cur = l2
                l2 = l2.next
            prev.next = cur
            prev = cur
        prev.next = l1 if l1 else l2
        return head
        
