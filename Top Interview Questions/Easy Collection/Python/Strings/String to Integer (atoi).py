class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = -1
        sign = 1
        ans = 0
        for ch in s:
            if ch == ' ':
                start += 1
            else:
                break
        s = s[start+1:]
        if not s:
            return 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        for ch in s:
            if ch >= '0' and ch <= '9':
                ans = ans * 10 + int(ch)
            else:
                break
        ans *= sign
        ans = 2**31-1 if ans > 2**31-1 else ans
        ans = -2**31 if ans < -2**31 else ans
        return ans
        
                
                
