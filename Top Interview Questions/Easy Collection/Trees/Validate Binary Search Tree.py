# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValid(self, root, low, high):
        if not root:
            return True
        if root.val <= low:
            return False
        if root.val >= high:
            return False
        return self.isValid(root.left, low, root.val) and self.isValid(root.right, root.val, high)
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, -2**31-1, 2**31)
        
