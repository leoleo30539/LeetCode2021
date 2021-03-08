class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        print(bin(n), len(bin(n))-2)
        ans = 0
        digit = 31
        while n > 0:
            if n%2 == 1: ans += 1
            ans <<= 1
            n //= 2
            digit -= 1
        if digit < 0:
            ans >>= abs(digit)
        else:
            ans <<= digit
        return ans
