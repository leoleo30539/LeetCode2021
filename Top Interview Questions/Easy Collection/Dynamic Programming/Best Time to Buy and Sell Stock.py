class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        low = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            elif prices[i] - low > ans:
                ans = prices[i] - low
        return ans
                
