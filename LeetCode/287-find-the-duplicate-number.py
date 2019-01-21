class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dups = {}
        for num in nums:
            if num in dups:
                return num
            dups[num] = 1
        return -1