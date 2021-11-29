class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_neg = True
        ans = 0
        temp_ans = 0
        for n in nums:
            if n > 0:
                all_neg = False
            if temp_ans >= 0:
                temp_ans += n
                if temp_ans > ans:
                    ans = temp_ans
            if temp_ans < 0:
                temp_ans = 0
        if all_neg:
            return max(nums)
        return ans
