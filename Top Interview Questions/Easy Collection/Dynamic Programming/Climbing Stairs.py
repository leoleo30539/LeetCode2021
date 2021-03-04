class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        if n == 2: return 2
        stair1, stair2 = 1, 2
        for i in range(n-2):
            stair2, stair1 = stair1+stair2, stair2
        return stair2
