class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x > 0 else -1
        x = abs(x)
        ans = 0
        while x > 0:
            if ans > (2**31-1)/10:
                return 0
            ans *= 10
            ans += x % 10
            x /= 10
        return ans * flag
