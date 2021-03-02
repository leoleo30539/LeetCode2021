class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = {}
        for ch in s:
            if ch not in ans:
                ans[ch] = 1
            else:
                ans[ch] += 1
        for i, ch in enumerate(s):
            if ans[ch] == 1:
                return i
        return -1
