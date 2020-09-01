class Solution:

  def findDisappearedNumbers(self, nums):
    """
        :type nums: List[int]
        :rtype: List[int]
        """
    found = {}
    for num in nums:
      found[num] = 1

    missing = []
    for i in range(1, len(nums) + 1):
      if i not in found:
        missing.append(i)
    return missing
