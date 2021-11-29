class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        l = min([len(s) for s in strs])
        word = strs[0]
        for i in range(l, 0, -1):
            ans = word[:i]
            flag = False
            for s in strs:
                if not s.startswith(ans):
                    flag = True
                    break
            if not flag:
                return ans
        return ""
