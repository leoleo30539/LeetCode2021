# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubSymmetric(self, left, right):
        if not left and not right:
            return True
        if not left and right:
            return False
        if left and not right:
            return False
        if left.val != right.val:
            return False
        return self.isSubSymmetric(left.right, right.left) and self.isSubSymmetric(left.left, right.right)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left and root.right:
            return False
        if root.left and not root.right:
            return False
        return self.isSubSymmetric(root.left, root.right)
