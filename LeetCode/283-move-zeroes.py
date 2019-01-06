class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[cur], nums[last_non_zero] = nums[last_non_zero], nums[cur]
                last_non_zero += 1