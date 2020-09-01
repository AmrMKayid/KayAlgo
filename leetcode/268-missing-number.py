class Solution:

  def missingNumber(self, nums):
    """
        :type nums: List[int]
        :rtype: int
        """
    missing = len(nums)
    for index, num in enumerate(nums):
      missing ^= index ^ num
    return missing
