class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        for i in nums:
            num ^= i
        return num