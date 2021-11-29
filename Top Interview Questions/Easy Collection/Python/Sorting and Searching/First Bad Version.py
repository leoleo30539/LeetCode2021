# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def findMid(self, start, end):
        if start == end-1:
            return end
        mid = int((start+end)/2)
        Bad = isBadVersion(mid)
        if Bad:
            return self.findMid(start, mid)
        else:
            return self.findMid(mid, end)
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        return self.findMid(1, n)
            
