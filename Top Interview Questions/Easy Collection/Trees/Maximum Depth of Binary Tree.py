# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left:
            return self.maxDepth(root.right)+1
        elif not root.right:
            return self.maxDepth(root.left)+1
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return left+1 if left > right else right+1
