# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        ans = []
        temp = [root.val]
        queue = [root]
        prev_level = 0
        level = [0]
        while queue:
            cur_level = level[0] + 1
            if cur_level != prev_level:
                ans.append(temp)
                temp = []
                prev_level = cur_level
            temp.append(queue[0].val)
            if queue[0].left:
                queue.append(queue[0].left)
                level.append(cur_level)
            if queue[0].right:
                queue.append(queue[0].right)
                level.append(cur_level)
            level.pop(0)
            queue.pop(0)
        ans.append(temp)
        ans.pop(0)
        return ans
