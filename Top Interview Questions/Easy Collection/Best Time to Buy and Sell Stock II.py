class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        flag = 0
        buy = 10001
        sell = -1
        for price in prices:
            if flag == 0:
                if price <= buy:
                    buy = price
                else:
                    flag = 1
                    sell = buy
            if flag == 1:
                if price > sell:
                    sell = price
                else:
                    profit += sell - buy
                    buy = price
                    flag = 0
        if flag == 1:
            profit += sell - buy
        return profit
