class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtracks(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtracks(S + '(', left + 1, right)
            if right < left:
                backtracks(S + ')', left, right + 1)

        backtracks()
        return ans
