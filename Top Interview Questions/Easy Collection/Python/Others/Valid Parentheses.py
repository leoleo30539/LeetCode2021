class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '{', '[']
        right = {')': '(', '}': '{', ']': '['}
        ans = []
        for char in s:
            if char in left: ans.append(char)
            else:
                if not ans: return False
                elif ans[-1] != right[char]: return False
                else: ans.pop()
        if not ans:
            return True
        return False
