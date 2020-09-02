class Solution:

  def heightChecker(self, heights: List[int]) -> int:
    moves = 0
    h = sorted(heights)
    for i in range(len(h)):
      if h[i] != heights[i]:
        moves += 1
    return moves
