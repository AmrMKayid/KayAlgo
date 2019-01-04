class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        n = len(nums)
        middle = n // 2
        if n % 2 == 0:
            return (nums[middle-1] + nums[middle]) / 2.0
        else:
            return nums[middle]