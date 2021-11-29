# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return None
        end_node = head
        del_node = head
        prev_node = head
        for i in range(n-1):
            end_node = end_node.next
        while end_node.next:
            prev_node = del_node
            del_node = del_node.next
            end_node = end_node.next
        if del_node == head:
            return head.next
        prev_node.next = del_node.next
        return head
