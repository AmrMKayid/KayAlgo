class Solution(object):

  def convert(self, s, numRows):
    """
        :type s: str
        :type numRows: int
        :rtype: str
        """
    if numRows == 1:
      return s

    str_levels = [""] * numRows
    currRow, plus = 0, 1
    for c in s:
      str_levels[currRow] += c
      currRow += plus
      if currRow == numRows - 1 or currRow == 0:
        plus *= -1
    return "".join(s for s in str_levels)
