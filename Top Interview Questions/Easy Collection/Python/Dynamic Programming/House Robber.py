class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        temp1 = nums[0]
        temp2 = max(nums[:2])
        temp3 = max([nums[2]+nums[0], nums[1]])
        for i in range(3, len(nums)):
            temp3, temp2, temp1 = max([nums[i-1]+temp1, nums[i]+temp2]), temp3, temp2
        return temp3
        
