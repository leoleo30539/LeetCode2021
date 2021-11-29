class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        ans = [0, 0, 1] + [1, 0] * int((n-2)/2)
        sqrt = int(n**0.5)
        for i in range(3, sqrt+1):
            if ans[i]:
                for j in range(i**2, n, i):
                    ans[j] = 0
        return sum(ans)
                
