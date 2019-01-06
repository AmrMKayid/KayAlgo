class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2**31 - 1 or x < -2**31:
            return 0
        reverse = int(str(x)[::-1]) if str(x)[0] != '-' else -1 * int(str(x)[1:][::-1])
        if reverse > 2**31 - 1 or reverse < -2**31:
            return 0
        return reverse

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        sign = 1 if x > 0 else -1
        x = x if x > 0 else -x
        while x != 0:
            rev = (rev * 10) + (x % 10)
            x /= 10
            # print(rev, x, sign)
            if rev >= 2**31 - 1 or rev <= -2**31:
                return 0
        return sign * rev