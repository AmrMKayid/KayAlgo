class Solution:

  def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums) <= 0:
      return 0
    index, unique = 0, nums[0]
    for i in range(1, len(nums)):
      if nums[i] == unique:
        i += 1
      else:
        index += 1
        unique = nums[i]
        nums[index] = unique
    return index + 1
