class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = 1
        for i in range(len(nums)-1):
            if nums[i+1] != nums[i]:
                nums[length] = nums[i+1]
                length += 1
        return length
