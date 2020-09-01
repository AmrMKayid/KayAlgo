class Solution(object):

  def expandAroundCenter(self, s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
      left -= 1
      right += 1
    return right - left - 1

  def longestPalindrome(self, s):
    """
        :type s: str
        :rtype: str
        """
    if not s:
      return ""
    n, start, end = len(s), 0, 0
    for i in range(n):
      len1, len2 = self.expandAroundCenter(s, i, i), self.expandAroundCenter(
          s, i, i + 1)
      length = max(len1, len2)
      if length > end - start:
        start = i - (length - 1) / 2
        end = i + length / 2
    return s[start:end + 1]
