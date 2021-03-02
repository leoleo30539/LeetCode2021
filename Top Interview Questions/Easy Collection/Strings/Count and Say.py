class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        temp = self.countAndSay(n-1)
        count = 0
        string = []
        count = []
        for t in temp:
            if not string or t != string[-1]:
                string.append(t)
                count.append(1)
            else:
                count[-1] += 1
        ans = ""
        for s, c in zip(string, count):
            ans += str(c) + s
        return ans
