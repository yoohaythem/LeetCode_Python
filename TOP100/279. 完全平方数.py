from math import sqrt


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]
        for i in range(1, n + 1):
            minimum = float("inf")
            for j in range(1, int(sqrt(i + 0.5)) + 1):
                minimum = min(minimum, dp[i - j ** 2])
            dp.append(minimum + 1)
        return dp[n]

