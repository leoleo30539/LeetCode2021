# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        if len(vals) == 1:
            return ListNode(vals[0])
        ans = ListNode(vals[-1])
        prev = ans
        vals = vals[:-1]
        for val in reversed(vals):
            cur = ListNode(val)
            prev.next = cur
            prev = cur
        return ans
        
