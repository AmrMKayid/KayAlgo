class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(((ord(c) - ord('A') + 1) * (26 ** exp) for exp, c in enumerate(s[::-1])))