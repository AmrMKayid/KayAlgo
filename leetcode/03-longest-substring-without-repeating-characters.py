class Solution(object):

  def lengthOfLongestSubstring(self, s):
    """
        :type s: str
        :rtype: int
        """
    char_dic = {}
    length, i, j, n = 0, 0, 0, len(s)
    for j in range(n):
      if s[j] in char_dic:
        i = max(i, char_dic[s[j]])
      length = max(length, j - i + 1)
      char_dic[s[j]] = j + 1
    return length
