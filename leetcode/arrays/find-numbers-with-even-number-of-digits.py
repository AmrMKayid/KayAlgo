class Solution:

  def findNumbers(self, nums: List[int]) -> int:
    even = 0
    for num in nums:
      len_dig = 0
      while num != 0:
        num //= 10
        len_dig += 1
      if len_dig % 2 == 0:
        even += 1
    return even
