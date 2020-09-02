class Solution:

  def removeElement(self, nums: List[int], val: int) -> int:
    i, length = 0, len(nums)
    while i < length:
      if nums[i] == val:
        length -= 1
        nums[i], nums[length] = nums[length], nums[i]
        i -= 1
      i += 1
    return length
