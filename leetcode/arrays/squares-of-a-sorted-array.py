class Solution:

  def sortedSquares(self, A: List[int]) -> List[int]:
    return sorted([num**2 for num in A])
