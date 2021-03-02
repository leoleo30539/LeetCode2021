class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = []
        for ch in s:
            if ch >= 'a' and ch <= 'z':
                temp.append(ord(ch))
            elif ch >= 'A' and ch <= 'Z':
                temp.append(ord(ch)-ord('A')+ord('a'))
            elif ch >= '0' and ch <= '9':
                temp.append(ord(ch))
        l = len(temp)
        for i in range(l/2):
            if temp[i] != temp[l-i-1]:
                return False
        return True
