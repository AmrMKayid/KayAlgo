class Solution(object):

  def hammingDistance(self, x, y):
    """
        :type x: int
        :type y: int
        :rtype: int
        """
    x_xor_y = x ^ y
    diff = 0
    while x_xor_y != 0:
      diff += x_xor_y % 2
      x_xor_y //= 2
    return diff
