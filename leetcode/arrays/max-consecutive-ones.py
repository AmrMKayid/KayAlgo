class Solution:

  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    i = max_ones = 0
    while i < len(nums):
      start = end = i
      while i < len(nums) and nums[i] == 1:
        end += 1
        i += 1
      max_ones = max(max_ones, end - start)
      i += 1
    return max_ones
