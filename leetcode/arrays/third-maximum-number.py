class Solution:

  def thirdMax(self, nums: List[int]) -> int:
    d = {}
    for num in nums:
      d[num] = 0
    nums = sorted(d.keys())
    if len(nums) <= 2:
      return max(nums)
    return nums[-3]
